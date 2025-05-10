from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from . import Role


class User(Base):
    username: Mapped[str] = mapped_column(String(20))
    userMiddleName: Mapped[str] = mapped_column(
        String(30), default="None", nullable=True
    )
    userLastName: Mapped[str] = mapped_column(String(30))
    userLogin: Mapped[str] = mapped_column(String(40), unique=True)
    userPassword: Mapped[str] = mapped_column(String(40))
    userPhone: Mapped[str] = mapped_column(String(25))
    userSpecialization: Mapped[str] = mapped_column(String(50))
    userScore: Mapped[int | None] = mapped_column(Integer, nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    userRole: Mapped["Role"] = relationship(back_populates="users")
    # users: Mapped[list["User"]] = relationship(back_populates="userRole")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)
