from fastapi import APIRouter

from exam_service.core.dependencies.fastapi import DatabaseDependency
from exam_service.lib.db import exam as exam_db
from exam_service.lib.schemas.exam import ExamCreateSchema, ExamSchema


router = APIRouter(tags=["exam"], prefix="/exams")


@router.post("/", response_model=ExamSchema)
async def create_exam(db: DatabaseDependency, schema: ExamCreateSchema) -> ExamSchema:
    return await exam_db.create_exam(db, schema=schema)
