from sqlalchemy import select, delete, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.Models import Task
from .schemas import CreateTask, UpdateTask


async def get_tasks(session: AsyncSession) -> list[Task]:
    stmt = select(Task).order_by(Task.id)
    result: Result = await session.execute(
        stmt
    )  # result равно выполненному запросу stmt

    tasks = result.scalars().all()  # scalar - функция, чтобы возвращалось
    # не кортеж, а объект, а all превращает в список
    return list(tasks)


async def get_task(session: AsyncSession, task_id: int) -> Task | None:
    return await session.get(Task, task_id)


async def remove_task(session: AsyncSession, task_id: int) -> str:
    query = delete(Task).where(Task.id == task_id)
    result: Result = await session.execute(query)
    await session.commit()
    return "Successful"


async def create_task(session: AsyncSession, task_in: CreateTask) -> Task:
    task = Task(**task_in.model_dump())
    # print("user", user.username)
    session.add(task)
    await session.commit()
    return task


async def update_task(session: AsyncSession, task_id: int, data: UpdateTask) -> str:
    query = (
        update(Task)
        .where(Task.id == task_id)
        .values(
            {
                Task.taskText: data.taskText,
                Task.taskScore: data.taskScore,
                Task.role_id: data.role_id,
                Task.status: data.status,
                Task.taskTitle: data.taskTitle,
                Task.assignedUserId: data.assignedUserId,
            }
        )
    )
    await session.execute(query)
    await session.commit()
    return "Successful update!"
