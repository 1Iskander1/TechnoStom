from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

#
from core.Models import db_helper
from . import crud
from .schemas import CreatePost, Post

router = APIRouter(tags=["Posts"])


@router.get("/", response_model=list[Post])
async def get_post(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_posts(session=session)


@router.post("/", response_model=Post)
async def create_post(
    post: CreatePost,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_post(session=session, post_in=post)
