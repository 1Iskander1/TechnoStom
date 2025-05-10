from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    taskText: str
    taskScore: int
    role_id: int


class UpdateTask(BaseModel):
    taskText: str
    taskScore: int
    role_id: int


class CreateTask(TaskBase):
    pass


class Task(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
