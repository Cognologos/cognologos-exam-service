from .abc import BaseSchema


class BaseCategorySchema(BaseSchema):
    name: str


class CategoryCreateSchema(BaseCategorySchema):
    name: str


class CategoriesSchema(BaseCategorySchema):
    id: int
    name: str
