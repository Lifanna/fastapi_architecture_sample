from fastapi import APIRouter
from api.users.users_router import router as users_router
from api.bikes.bikes_router import router as bikes_router

api_router = APIRouter()

api_router.include_router(
    users_router,
    prefix="/api",
)

api_router.include_router(
    bikes_router,
    prefix="/api",
)
