import datetime

from pydantic import BaseModel


class UserIn(BaseModel):
    id: int
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_verified: bool
    created_at: datetime.datetime

