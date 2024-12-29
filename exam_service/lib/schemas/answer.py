from .abc import BaseSchema


class BaseAnswerSchema(BaseSchema):
    answer: str


class AnswerCreateSchema(BaseAnswerSchema):
    answer: str


class AnswerSchema(BaseAnswerSchema):
    id: int
    question_id: int
    result_id: int
    answer: str
