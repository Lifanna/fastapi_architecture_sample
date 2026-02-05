from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.users_schemas import UserCreate, UserRead
from data_access.db.session import get_db
from data_access.users.users_repository import UsersRepository
from business_logic.users.users_service import UsersService

router = APIRouter()


def get_users_service(db: AsyncSession = Depends(get_db)) -> UsersService:
    repo = UsersRepository(db)
    return UsersService(repo)


@router.get("/", response_model=list[UserRead])
async def get_users(
    service: UsersService = Depends(get_users_service),
):
    return await service.get_users()


@router.post("/", response_model=UserRead)
async def create_user(
    user: UserCreate,
    service: UsersService = Depends(get_users_service),
):
    try:
        return await service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
