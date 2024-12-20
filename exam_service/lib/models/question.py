from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .abc import AbstractModel


class QuestionModel(AbstractModel):
    __tablename__ = "questions"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"))
    text: Mapped[str]
