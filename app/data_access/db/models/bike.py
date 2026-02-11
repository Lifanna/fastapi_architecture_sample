from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data_access.db.base import Base


class Bike(Base):
    __tablename__ = "bikes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column()
    image_path: Mapped[str] = mapped_column(String(255))

    # Связь с брендом
    brand_id: Mapped[int] = mapped_column(ForeignKey("bike_brands.id"))
    brand: Mapped["BikeBrand"] = relationship("BikeBrand", back_populates="bikes")
