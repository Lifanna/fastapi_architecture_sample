from fastapi import APIRouter
from . import bikes_api

router = APIRouter(
    prefix="/bikes",
)

router.include_router(
    bikes_api.router,
    tags=["bikes"],
)
