from .abc import BaseSchema


class BaseAnswerSchema(BaseSchema):
    answer: str


class AnswerCreateSchema(BaseAnswerSchema):
    answer: str


class AnswersSchema(BaseAnswerSchema):
    id: int
    question_id: int
    result_id: int
    answer: str
    
