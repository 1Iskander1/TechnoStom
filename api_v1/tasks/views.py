from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import db_helper
from . import crud
from .schemas import Task, CreateTask, UpdateTask

router = APIRouter(tags=["Tasks"])


@router.get("/", response_model=list[Task])
async def get_tasks(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_tasks(session=session)


@router.get("/{task_id}", response_model=Task)
async def get_task(
    task_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    task = await crud.get_task(task_id=task_id, session=session)
    if task is not None:
        return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {task_id} not found!",
    )


@router.delete("/{task_id}")
async def remove_task(
    task_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    task = await crud.remove_task(task_id=task_id, session=session)
    if task is not None:
        return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {task_id} not found!",
    )


@router.post("/", response_model=Task)
async def create_task(
    task: CreateTask,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_task(session=session, task_in=task)


@router.patch("/{task_id}")
async def update_task(
    data: UpdateTask,
    task_id: int,
    # session: AsyncSession = db_helper.session_factory(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    task = await crud.get_task(task_id=task_id, session=session)
    if task is not None:
        return await crud.update_task(session=session, data=data, task_id=task_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Role {task_id} not found!",
    )
