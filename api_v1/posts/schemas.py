from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    body: str
    user_id: int


class CreatePost(PostBase):
    pass


class Post(PostBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
