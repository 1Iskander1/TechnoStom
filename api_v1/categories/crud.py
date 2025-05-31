from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import Category
from .schemas import CategoryCreate


async def get_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    categories = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    # print(list(categories))
    return list(categories)


async def get_category(session: AsyncSession, category_id: int) -> Category | None:
    return await session.get(Category, category_id)


async def create_category(
    session: AsyncSession, category_in: CategoryCreate
) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    # await session.refresh(product)
    return category


# async def remove_category(session: AsyncSession, category_id: int) -> Category | None:
#     return await session.delete(Category)
