from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.Models import User as UserModel  # SQLAlchemy модель
from core.Models import db_helper
from . import crud

# from .schemas import CreateUser, User, UpdateUser, LoginData
from .schemas import (
    LoginData,
    User as UserSchema,
    UpdateUser,
    CreateUser,
)  # Pydantic схема

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserSchema])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session=session)


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await crud.get_user(user_id=user_id, session=session)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {user_id} not found!",
    )


@router.delete("/{user_id}")
async def remove_user(
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await crud.remove_user(user_id=user_id, session=session)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {user_id} not found!",
    )


@router.post("/", response_model=UserSchema)
async def create_user(
    user: CreateUser,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(session=session, user_in=user)


@router.patch("/{user_id}")
async def update_user(
    data: UpdateUser,
    user_id: int,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await crud.get_user(user_id=user_id, session=session)
    if user is not None:
        return await crud.update_user(session=session, data=data, user_id=user_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {user_id} not found!",
    )


@router.post("/auth/login", response_model=UserSchema)
async def login(
    login_data: LoginData,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    # Оптимизированный запрос с жадной загрузкой роли
    stmt = (
        select(UserModel)
        .options(selectinload(UserModel.userRole))  # Теперь импортирован
        .where(
            (UserModel.userLogin == login_data.Login)
            & (UserModel.userPassword == login_data.Password)
        )
    )

    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    # Проверяем роль через relationship
    if user.userRole.roleTitle != "Администратор":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied (not admin)"
        )

    return user


@router.post("/auth/login/employer", response_model=UserSchema)
async def login_employer(
    login_data: LoginData,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    # Оптимизированный запрос с жадной загрузкой роли
    stmt = (
        select(UserModel)
        .options(selectinload(UserModel.userRole))  # Теперь импортирован
        .where(
            (UserModel.userLogin == login_data.Login)
            & (UserModel.userPassword == login_data.Password)
        )
    )

    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    # Проверяем роль через relationship
    if user.userRole.roleTitle == "Администратор":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied (not admin)"
        )

    return user
