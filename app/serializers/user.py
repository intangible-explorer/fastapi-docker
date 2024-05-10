from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str
    is_active: bool

    class Config:
        from_attributes = True


class CreateUserSerializer(UserBase):
    pass

class RetrieveUserSerializer(UserBase):
    id: int

    class Config:
        from_attributes = True

class ListUserSerializer(BaseModel):
    users: List[RetrieveUserSerializer]

    class Config:
        from_attributes = True