from pydantic import BaseModel
from typing import List

from models.users import User


class Message(BaseModel):
    """
    status = 1: request success
    status = 0: request fail
    """
    status: int
    data: List[User]
    msg: str
