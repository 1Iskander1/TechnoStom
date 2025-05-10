from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    userMiddleName: str
    userLastName: str
    userLogin: str
    userPassword: str
    userPhone: str
    role_id: int
    userSpecialization: str
    userScore: int | None


class UpdateUser(BaseModel):
    username: str
    userMiddleName: str
    userLastName: str
    userPhone: str
    userSpecialization: str


class CreateUser(UserBase):
    pass


class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
