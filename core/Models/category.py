from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from . import Material


class Category(Base):
    categoryTitle: Mapped[str] = mapped_column(String(30))
    materials: Mapped[list["Material"]] = relationship(
        back_populates="materialCategory"
    )
