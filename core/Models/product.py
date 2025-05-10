from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Product(Base):
    name = mapped_column(String(50))
    price: Mapped[int]
