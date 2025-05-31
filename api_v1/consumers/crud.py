from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import Consumer
from .schemas import ConsumerCreate


async def get_consumers(session: AsyncSession) -> list[Consumer]:
    stmt = select(Consumer).order_by(Consumer.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    consumer = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    # print(list(roles))
    return list(consumer)


async def get_consumer(session: AsyncSession, consumer_id: int) -> Consumer | None:
    return await session.get(Consumer, consumer_id)


async def create_consumer(
    session: AsyncSession, consumer_in: ConsumerCreate
) -> Consumer:
    consumer = Consumer(**consumer_in.model_dump())
    session.add(consumer)
    await session.commit()
    # await session.refresh(product)
    return consumer
