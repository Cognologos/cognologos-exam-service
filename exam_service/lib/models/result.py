from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .abc import AbstractModel
if TYPE_CHECKING:
    from .answer import AnswerModel
    from .exam import ExamModel


class ResultModel(AbstractModel):
    __tablename__ = "results"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"))
    answers: Mapped[list["AnswerModel"]] = relationship("AnswerModel", back_populates="results")
    exam: Mapped["ExamModel"] = relationship("ExamModel", back_populates="results")