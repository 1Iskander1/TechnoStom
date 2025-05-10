from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import db_helper
from . import crud
from .schemas import RoleCreate, Role

router = APIRouter(tags=["Roles"])


@router.get("/", response_model=list[Role])
async def get_roles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_roles(session=session)


@router.post("/", response_model=Role)
async def create_role(
    role_in: RoleCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_role(session=session, role_in=role_in)


@router.get("/{role_id}", response_model=Role)
async def get_role(
    role_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    role = await crud.get_role(role_id=role_id, session=session)
    if role is not None:
        return role
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {role_id} not found!",
    )
