from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import db_helper
from . import crud
from .schemas import CategoryCreate, Category

router = APIRouter(tags=["Categorys"])


@router.get("/", response_model=list[Category])
async def get_categories(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_categories(session=session)


@router.post("/", response_model=Category)
async def create_category(
    category_in: CategoryCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_category(session=session, category_in=category_in)


@router.get("/{category_id}", response_model=Category)
async def get_category(
    category_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    category = await crud.get_category(category_id=category_id, session=session)
    if category is not None:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category {category_id} not found!",
    )
