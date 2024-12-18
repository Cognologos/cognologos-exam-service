"""Problem model."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .abc import AbstractModel



class ProblemModel(AbstractModel):
    """The problems model."""

    __tablename__ = "categories"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    """ID of the problem."""
    name: Mapped[str]
    """Text of the problem."""
    category_id: Mapped[int] = mapped_column(ForeignKey("exams.id"))
    """ID of the associated exam, FK."""