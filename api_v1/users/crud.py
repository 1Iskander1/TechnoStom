from sqlalchemy import select, delete, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import User
from .schemas import CreateUser, UpdateUser


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    users = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def remove_user(session: AsyncSession, user_id: int) -> str:
    query = delete(User).where(User.id == user_id)
    result: Result = await session.execute(query)
    await session.commit()
    return "Successful"


async def update_user(session: AsyncSession, user_id: int, data: UpdateUser) -> str:
    query = (
        update(User)
        .where(User.id == user_id)
        .values(
            {
                User.username: data.username,
                User.userMiddleName: data.userMiddleName,
                User.userLastName: data.userLastName,
                User.userSpecialization: data.userSpecialization,
                User.userPhone: data.userPhone,
            }
        )
    )
    await session.execute(query)
    await session.commit()
    return "Successful update!"


async def create_user(session: AsyncSession, user_in: CreateUser) -> User:
    user = User(**user_in.model_dump())
    # print("user", user.username)
    session.add(user)
    await session.commit()
    return user


# async def main():
#     async with db_helper.session_factory() as session:
#         await create_user(session=session, username="John")
#         await create_user(session=session, username="Sam")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
