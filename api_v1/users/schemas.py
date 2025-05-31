from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    userMiddleName: str
    userLastName: str
    userLogin: str
    userPassword: str
    userPhone: str
    role_id: int

    userScore: int | None


class UpdateUser(BaseModel):
    username: str
    userMiddleName: str
    userLastName: str
    userPhone: str


class CreateUser(UserBase):
    pass


class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LoginData(BaseModel):
    Login: str
    Password: str
