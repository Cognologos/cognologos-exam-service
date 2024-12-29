from fastapi import APIRouter
from . import exam


router = APIRouter(prefix="/v1")

for i in [
    exam.router
]:
    router.include_router(i)
