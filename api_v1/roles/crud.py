from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import Role
from .schemas import RoleCreate


async def get_roles(session: AsyncSession) -> list[Role]:
    stmt = select(Role).order_by(Role.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    roles = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    # print(list(roles))
    return list(roles)


async def get_role(session: AsyncSession, role_id: int) -> Role | None:
    return await session.get(Role, role_id)


async def create_role(session: AsyncSession, role_in: RoleCreate) -> Role:
    role = Role(**role_in.model_dump())
    session.add(role)
    await session.commit()
    # await session.refresh(product)
    return role


# async def remove_role(session: AsyncSession, role_id: int) -> Role | None:
#     return await session.delete(Role)
