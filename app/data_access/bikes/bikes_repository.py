from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models import Bike
from sqlalchemy.orm import selectinload


class BikesRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Bike]:
        result = await self.db.execute(
            select(Bike).options(selectinload(Bike.brand))
        )
        return result.scalars().all()

    async def get_by_id(self, user_id: int) -> Bike | None:
        result = await self.db.execute(
            select(Bike).where(Bike.id == user_id)
        )
        return result.scalar_one_or_none()

    async def create(self, user: Bike) -> Bike:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
