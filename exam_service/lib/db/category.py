from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from exam_service.core.exceptions.category import CategoryNotFoundException, CategoryNameAlreadyExistsException
from exam_service.lib.models import CategoryModel
from exam_service.lib.schemas.category import CategoryCreateSchema, CategorySchema


async def is_category_exists(db: AsyncSession, name: str) -> bool:
    query = select(CategoryModel).where(CategoryModel.name == name)
    return bool((await db.execute(query)).scalar_one_or_none())


async def raise_for_category_name(db: AsyncSession, name: str) -> None:
    if await is_category_exists(db, name):
        raise CategoryNameAlreadyExistsException(name=name)


async def create_category(
    db: AsyncSession,
    *,
    schema: CategoryCreateSchema,
) -> CategorySchema:
    await raise_for_category_name(db, schema.name)

    category_model = CategoryModel(**schema.model_dump())
    db.add(category_model)
    await db.flush()
    return CategorySchema.model_construct(**category_model.to_dict())


async def get_category_model(
    db: AsyncSession,
    *,
    name: str,
) -> CategoryModel:
    query = select(CategoryModel).where(CategoryModel.name == name)
    result = (await db.execute(query)).scalar_one_or_none()
    if result is None:
        raise CategoryNotFoundException
    return result


async def get_category_model_by_id(
    db: AsyncSession,
    *,
    category_id: int,
) -> CategoryModel:
    query = select(CategoryModel).where(CategoryModel.id == category_id)
    result = (await db.execute(query)).scalar_one_or_none()
    if result is None:
        raise CategoryNotFoundException
    return result


async def get_category(
    db: AsyncSession,
    *,
    category_id: int,
) -> CategorySchema:
    query = select(CategoryModel).where(CategoryModel.id == category_id)
    user_model = (await db.execute(query)).scalar_one_or_none()
    if user_model is None:
        raise CategoryNotFoundException
    return CategorySchema.model_construct(**user_model.to_dict())


async def delete_category(
    db: AsyncSession,
    *,
    category_id: int,
) -> None:
    category_model = await get_category_model_by_id(db, category_id=category_id)

    await db.flush()
