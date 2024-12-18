from typing import Annotated, Any, AsyncGenerator
from uuid import UUID

from exam_service.core.config import AppConfig
from fastapi import Cookie, Depends, Header, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from redis.asyncio import ConnectionPool, Redis as AbstractRedis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from ..security import Encryptor
from . import constructors as app_depends


def db_session_maker_stub() -> sessionmaker[Any]:
    raise NotImplementedError


def app_config_stub() -> AppConfig:
    raise NotImplementedError


async def db_session(
    request: Request,
    maker: Annotated[sessionmaker[Any], Depends(db_session_maker_stub)],
) -> AsyncGenerator[AsyncSession, None]:
    generator = app_depends.db_session_autocommit(maker)
    session = await anext(generator)
    request.state.db = session

    yield session

    try:
        await anext(generator)
    except StopAsyncIteration:
        pass
    else:
        raise RuntimeError("Database session not closed (db dependency generator is not closed).")


def redis_conn_pool_stub() -> ConnectionPool:
    raise NotImplementedError


async def redis_conn(
    request: Request, conn_pool: Annotated[ConnectionPool, Depends(redis_conn_pool_stub)]
) -> AsyncGenerator[AbstractRedis, None]:
    generator = app_depends.redis_conn(conn_pool)
    redis = await anext(generator)
    request.state.redis = redis

    yield redis

    try:
        await anext(generator)
    except StopAsyncIteration:
        pass
    else:
        raise RuntimeError("Redis session not closed (redis dependency generator is not closed).")


def get_client_host(request: Request) -> str:
    client = request.client
    return client.host if client else ""



ClientHostDependency = Annotated[str, Depends(get_client_host)]
UserAgentDependency = Annotated[str, Header()]
DatabaseDependency = Annotated[AsyncSession, Depends(db_session)]
RedisDependency = Annotated[AbstractRedis, Depends(redis_conn)]
