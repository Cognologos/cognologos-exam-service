from .abc import BaseSchema


class BaseQuestionSchema(BaseSchema):
    text: str


class QuestionCreateSchema(BaseQuestionSchema):
    exam_id: int
    text: str


class QuestionsSchema(BaseQuestionSchema):
    id: int
    exam_id: int
    text: str
