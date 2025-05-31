# Этот файл описывает таблицы
from pydantic import BaseModel, ConfigDict


class ConsumerBase(BaseModel):
    consumerTitle: str


class ConsumerCreate(ConsumerBase):
    pass


class Consumer(ConsumerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
