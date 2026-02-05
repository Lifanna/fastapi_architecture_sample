from fastapi import APIRouter
from . import users_api

router = APIRouter(
    prefix="/users",
)

router.include_router(
    users_api.router,
    tags=["users"],
)
