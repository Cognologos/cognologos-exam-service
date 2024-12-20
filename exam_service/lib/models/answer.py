from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .abc import AbstractModel

if TYPE_CHECKING:
    from .result import ResultModel


class AnswerModel(AbstractModel):
    __tablename__ = "answers"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    result_id: Mapped[int] = mapped_column(ForeignKey("results.id"))
    answer: Mapped[str]
    results: Mapped[list["ResultModel"]] = relationship("ResultModel", back_populates="results")
