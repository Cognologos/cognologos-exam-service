from datetime import datetime

from .abc import BaseSchema
from .answer import AnswerCreateSchema


class BaseResultSchema(BaseSchema):
    pass


class ResultCreateSchema(BaseResultSchema):
    exam_id: int
    answers: list[AnswerCreateSchema]


class ResultSchema(BaseResultSchema):
    id: int
    exam_id: int
    user_id: int
    created_at: datetime


class ResultTotalsSchema(BaseResultSchema):
    id: int
    exam_id: int
    user_id: int
    total_problems: int
    right_answers: int
    free_answers: int
