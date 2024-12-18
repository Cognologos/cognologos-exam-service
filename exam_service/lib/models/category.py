from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from .abc import AbstractModel


class CategoryModel(AbstractModel):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str]

