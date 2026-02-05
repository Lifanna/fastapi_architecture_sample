from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # для SQLAlchemy моделей
