from data_access.users.users_repository import UsersRepository
from data_access.db.models import User
from api.users.users_schemas import UserCreate


class UsersService:
    def __init__(self, repo: UsersRepository):
        self.repo = repo

    async def get_users(self):
        return await self.repo.get_all()

    async def get_user_by_id(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    async def create_user(self, data: UserCreate):
        # здесь может быть любая бизнес-логика
        # проверки, логирование, интеграции и т.п.

        user = User(
            name=data.name,
            email=data.email
        )
        return await self.repo.create(user)
