# Этот файл описывает таблицы
from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    roleTitle: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
