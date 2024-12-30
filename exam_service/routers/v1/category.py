from fastapi import APIRouter

from exam_service.core.dependencies.fastapi import DatabaseDependency
from exam_service.lib.db import category as category_db
from exam_service.lib.schemas.category import CategoryCreateSchema, CategorySchema


router = APIRouter(tags=["category"], prefix="/categories")


@router.post("/", response_model=CategorySchema)
async def create_category(db: DatabaseDependency, schema: CategoryCreateSchema) -> CategorySchema:
    return await category_db.create_category(db, schema=schema)


@router.get("/get_exam", response_model=CategorySchema)
async def get_user(db: DatabaseDependency, category_id: int) -> CategorySchema:
    return await category_db.get_category(db, category_id=category_id)


@router.delete("/get_exam", status_code=204)
async def delete_exam(db: DatabaseDependency, category_id: int) -> None:
    return await category_db.delete_category(db, category_id=category_id)
