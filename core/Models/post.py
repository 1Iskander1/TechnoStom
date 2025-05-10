# from typing import TYPE_CHECKING
#
# from sqlalchemy import Text, String
# from sqlalchemy.orm import mapped_column, Mapped
#
# from .base import Base
#
# if TYPE_CHECKING:
#     pass
#
#
# class Post(Base):
#     # _user_back_populates = "posts"
#     # _user_id_nullable = True
#     title: Mapped[str] = mapped_column(String(100))
#     body: Mapped[str] = mapped_column(
#         Text,
#     )
