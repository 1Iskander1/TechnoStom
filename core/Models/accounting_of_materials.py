from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from . import Category


class Material(Base):
    materialTitle: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int]
    unit: Mapped[str] = mapped_column(String(10))  # единица измерения
    min_stock_level: Mapped[int]  # Минимальный запас, при котором требуется заказ.
    category: Mapped[int] = mapped_column(ForeignKey("categorys.id"))
    status: Mapped[str] = mapped_column(String(25))
    materialCategory: Mapped["Category"] = relationship(back_populates="materials")
