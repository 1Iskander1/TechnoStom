from typing import TYPE_CHECKING

from sqlalchemy import Text, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from . import Role


class Task(Base):
    # 2 таблица задания (роль, само задание, сколько баллов получит сотрудник),
    taskText: Mapped[str] = mapped_column(
        Text,
    )
    taskScore: Mapped[int] = mapped_column(Integer)
    # username: Mapped[str] = mapped_column(String(20))
    # userMiddleName: Mapped[str] = mapped_column(
    #     String(30), default="None", nullable=True
    # )
    # userLastName: Mapped[str] = mapped_column(String(30))
    # userLogin: Mapped[str] = mapped_column(String(40), unique=True)
    # userPassword: Mapped[str] = mapped_column(String(40))
    # userPhone: Mapped[str] = mapped_column(String(25))
    # userSpecialization: Mapped[str] = mapped_column(String(50))
    # userScore: Mapped[int | None] = mapped_column(Integer, nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    taskRole: Mapped["Role"] = relationship(back_populates="task")
    # users: Mapped[list["User"]] = relationship(back_populates="userRole")
