from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    pass


class Consumer(Base):
    consumerTitle: Mapped[str] = mapped_column(String(50))
