# from typing import TYPE_CHECKING
#
# from sqlalchemy import String, Text
# from sqlalchemy.orm import mapped_column, Mapped
#
# from .base import Base
#
# if TYPE_CHECKING:
#     pass
#
#
# class Profile(Base):
#     # _user_id_unique = True
#     # _user_back_populates = "profile"
#
#     firstname: Mapped[str | None] = mapped_column(String(40))
#     lastname: Mapped[str | None] = mapped_column(String(40))
#     bio: Mapped[str | None] = mapped_column(Text)
