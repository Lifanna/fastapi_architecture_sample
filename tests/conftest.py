import pytest
from httpx import AsyncClient
from fastapi import FastAPI

from app.api.users.users_api import router as users_router


@pytest.fixture
def app():
    app = FastAPI()
    app.include_router(users_router)
    return app


@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
