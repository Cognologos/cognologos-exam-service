from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .abc import AbstractModel


class AnswerModel(AbstractModel):
    __tablename__ = "answers"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    result_id: Mapped[int] = mapped_column(ForeignKey("results.id"))
    answer: Mapped[str]
