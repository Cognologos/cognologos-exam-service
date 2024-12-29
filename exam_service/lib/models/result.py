from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .abc import AbstractModel


if TYPE_CHECKING:
    from .answer import AnswerModel
    from .exam import ExamModel


class ResultModel(AbstractModel):
    __tablename__ = "results"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    user_id: Mapped[int]
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    answers: Mapped[list["AnswerModel"]] = relationship("AnswerModel", back_populates="results")
    exam: Mapped["ExamModel"] = relationship("ExamModel", back_populates="results")
