from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .abc import AbstractModel


if TYPE_CHECKING:
    from .category import CategoryModel
    from .question import QuestionModel
    from .result import ResultModel


class ExamModel(AbstractModel):
    __tablename__ = "exams"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str | None]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    questions: Mapped[list["QuestionModel"]] = relationship(
        "QuestionModel", back_populates="exam", cascade="all, delete-orphan"
    )
    results: Mapped[list["ResultModel"]] = relationship(
        "ResultModel", back_populates="exam", cascade="all, delete-orphan"
    )
    category: Mapped[list["CategoryModel"]] = relationship("CategoryModel")
