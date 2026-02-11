from data_access.bikes.bikes_repository import BikesRepository
from data_access.db.models import Bike
from api.bikes.bikes_schemas import BikeCreate


class BikesService:
    def __init__(self, repo: BikesRepository):
        self.repo = repo

    async def get_bikes(self):
        return await self.repo.get_all()

    async def get_bike_by_id(self, bike_id: int):
        bike = await self.repo.get_by_id(bike_id)
        if not bike:
            raise ValueError("Bike not found")
        return bike

    async def create_bike(self, data: BikeCreate):
        bike = Bike(
            name=data.name,
            price=data.price,
            image_path=data.image_path,
            brand_id=data.brand_id,
        )
        return await self.repo.create(bike)
