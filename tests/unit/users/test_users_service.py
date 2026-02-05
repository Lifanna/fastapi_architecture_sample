import pytest
from unittest.mock import AsyncMock

from app.business_logic.users.users_service import UsersService
from app.api.users.users_schemas import UserCreate
from app.data_access.db.models import User


@pytest.mark.asyncio
async def test_create_user():
    repo = AsyncMock()
    service = UsersService(repo)

    repo.create.return_value = User(
        id=1,
        name="Test",
        email="test@mail.com"
    )

    data = UserCreate(
        name="Test",
        email="test@mail.com"
    )

    user = await service.create_user(data)

    assert user.id == 1
    assert user.email == "test@mail.com"
    repo.create.assert_called_once()
