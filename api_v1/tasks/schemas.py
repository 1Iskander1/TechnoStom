from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    taskTitle: str
    taskText: str
    taskScore: int
    role_id: int
    status: str
    assignedUserId: int


class UpdateTask(BaseModel):
    taskTitle: str
    taskText: str
    taskScore: int
    role_id: int
    status: str
    assignedUserId: int


class CreateTask(TaskBase):
    pass


class Task(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
