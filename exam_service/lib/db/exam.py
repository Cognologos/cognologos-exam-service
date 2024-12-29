from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from exam_service.core.exceptions.exam import ExamNotFoundException, ExamNameAlreadyExistsException
from exam_service.lib.models import ExamModel
from exam_service.lib.schemas.exam import ExamCreateSchema, ExamSchema


async def is_exam_exists(db: AsyncSession, name: str) -> bool:
    query = select(ExamModel).where(ExamModel.name == name)
    return bool((await db.execute(query)).scalar_one_or_none())


async def raise_for_exam_name(db: AsyncSession, name: str) -> None:
    if await is_exam_exists(db, name):
        raise ExamNameAlreadyExistsException(name=name)


async def create_exam(
    db: AsyncSession,
    *,
    schema: ExamCreateSchema,
) -> ExamSchema:
    await raise_for_exam_name(db, schema.name)

    exam_model = ExamModel(
        **schema.model_dump()
    )
    db.add(exam_model)
    await db.flush()
    return ExamSchema.model_construct(**exam_model.to_dict())


async def get_exam_model(
    db: AsyncSession,
    *,
    name: str,
) -> ExamModel:
    query = select(ExamModel).where(ExamModel.name == name)
    result = (await db.execute(query)).scalar_one_or_none()
    if result is None:
        raise ExamNotFoundException
    return result


async def get_exam_model_by_id(
    db: AsyncSession,
    *,
    exam_id: int,
) -> ExamModel:
    query = select(ExamModel).where(ExamModel.id == exam_id)
    result = (await db.execute(query)).scalar_one_or_none()
    if result is None:
        raise ExamNotFoundException
    return result


async def get_exam(
    db: AsyncSession,
    *,
    exam_id: int,
) -> ExamSchema:
    query = select(ExamModel).where(ExamModel.id == exam_id)
    user_model = (await db.execute(query)).scalar_one_or_none()
    if user_model is None:
        raise ExamNotFoundException
    return ExamSchema.model_construct(**user_model.to_dict())


async def delete_exam(
    db: AsyncSession,
    *,
    exam_id: int,
) -> None:
    exam_model = await get_exam_model_by_id(db, exam_id=exam_id)
    exam_model.deleted_at = datetime.now(timezone.utc)

    await db.flush()
