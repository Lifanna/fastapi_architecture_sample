from typing import Optional
from pydantic import BaseModel, EmailStr


class BikeCreate(BaseModel):
    name: str
    brand_id: int         # ссылка на существующий бренд
    price: float
    image_path: Optional[str] = None

class BikeBrandRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BikeRead(BaseModel):
    id: int
    name: str
    price: float
    image_path: Optional[str]
    brand: BikeBrandRead  # вложенный объект

    class Config:
        orm_mode = True
