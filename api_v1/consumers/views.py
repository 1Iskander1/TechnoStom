from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import db_helper
from . import crud
from .schemas import ConsumerCreate, Consumer

router = APIRouter(tags=["Consumers"])


@router.get("/", response_model=list[Consumer])
async def get_consumers(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_consumers(session=session)


@router.post("/", response_model=Consumer)
async def create_consumers(
    consumer_in: ConsumerCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_consumer(session=session, consumer_in=consumer_in)


@router.get("/{consumer_id}", response_model=Consumer)
async def get_consumer(
    consumer_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    consumer = await crud.get_consumer(consumer_id=consumer_id, session=session)
    if consumer is not None:
        return consumer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Consumer {consumer_id} not found!",
    )
