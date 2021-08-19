from pydantic import BaseModel

class User(BaseModel):
    id: int
    user_name: str
    first_name: str
    last_name: str
    password: str
    email: str
    institution: str
    country: str


class UserRegister(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    password: str
    email: str
    institution: str
    country: str


class UserLogin(BaseModel):
    user_name: str
    password: str
