from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import Post
from .schemas import CreatePost


async def get_posts(session: AsyncSession) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    posts = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    return list(posts)


# async def get_post(session: AsyncSession, product_id: int) -> Post | None:
#     return await session.get(Post, product_id)


async def create_post(session: AsyncSession, post_in: CreatePost) -> Post:
    product = Post(**post_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product
