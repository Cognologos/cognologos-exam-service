from datetime import datetime

from .abc import BaseSchema


class BaseExamSchema(BaseSchema):
    name: str


class ExamCreateSchema(BaseExamSchema):
    name: str
    description: str 
    category_id: int

class ExamSchema(BaseExamSchema):
    id: int
    name: str
    description: bool
    category_id: int
    created_at: datetime
