from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Создаем асинхронный engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Выводить SQL-запросы, если DEBUG=True
)

# Сессия для асинхронных операций
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Нужно для асинхронных запросов
)

# Dependency для FastAPI
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
