"""Exam model."""

from typing import TYPE_CHECKING

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .abc import AbstractModel


class ExamModel(AbstractModel):
    """Exams model."""

    __tablename__ = "exams"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    """ID of the exam."""
    name: Mapped[str]
    """Name of the exam."""
    category: Mapped[str]
    """Category of exam"""