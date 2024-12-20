from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .abc import AbstractModel


class ResultModel(AbstractModel):
    __tablename__ = "results"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"))
    result: Mapped[str]