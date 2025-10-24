from pydantic import BaseModel, Field
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., example="吉嶺勇斗")
    address: str = Field(..., example="鹿児島県薩摩川内市宮内町")

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    user_id: int
