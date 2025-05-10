from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base

if TYPE_CHECKING:
    from . import User, Task


class Role(Base):
    roleTitle: Mapped[str] = mapped_column(String(30))
    # users: Mapped[list[User]] = mapped_column()

    users: Mapped[list["User"]] = relationship(back_populates="userRole")
    task: Mapped[list["Task"]] = relationship(back_populates="taskRole")
