from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.bikes.bikes_schemas import BikeCreate, BikeRead
from business_logic.bikes.bikes_service import BikesService
from data_access.bikes.bikes_repository import BikesRepository
from data_access.db.session import get_db

router = APIRouter()


def get_bikes_service(db: AsyncSession = Depends(get_db)) -> BikesService:
    repo = BikesRepository(db)
    return BikesService(repo)


@router.get("/", response_model=list[BikeRead])
async def get_bikes(
    service: BikesService = Depends(get_bikes_service),
):
    return await service.get_bikes()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_bike(
    bike: BikeCreate,
    service: BikesService = Depends(get_bikes_service),
):
    try:
        return await service.create_bike(bike)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
