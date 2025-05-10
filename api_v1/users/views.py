from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import db_helper
from . import crud
from .schemas import CreateUser, User, UpdateUser

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session=session)


@router.get("/{user_id}", response_model=User)
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


@router.post("/", response_model=User)
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
