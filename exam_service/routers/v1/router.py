from fastapi import APIRouter
from . import exam, category


router = APIRouter(prefix="/v1")

for i in [
    exam.router,
    category.router,
]:
    router.include_router(i)
