from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data_access.db.base import Base


class BikeBrand(Base):
    __tablename__ = "bike_brands"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    bikes: Mapped[list["Bike"]] = relationship("Bike", back_populates="brand")
