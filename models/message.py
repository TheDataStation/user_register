from pydantic import BaseModel
from typing import List

from models.users import User


class Message(BaseModel):
    status: int
    data: List[User]
    msg: str
