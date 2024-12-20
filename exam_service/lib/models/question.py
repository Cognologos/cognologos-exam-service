from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .abc import AbstractModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exam import ExamModel


class QuestionModel(AbstractModel):
    __tablename__ = "questions"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"))
    text: Mapped[str]
    exam: Mapped["ExamModel"] = relationship("ExamModel", back_populates="questions")