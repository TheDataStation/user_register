from fastapi import APIRouter
from typing import List
from db_config import database
from models.users import User, UserIn, users
from models.message import Message
import bcrypt

router = APIRouter()


@router.get("/users/", response_model=List[User])
async def get_all_users():
    query = users.select()
    return await database.fetch_all(query)


@router.post("/users/user_name", response_model=User)
async def get_user_by_user_name(username: str):
    query = users.select().where(users.c.user_name == username)
    return await database.fetch_one(query)


@router.post("/users/", response_model=Message)
async def create_user(user: UserIn):
    # check if there is an existing user
    query = users.select().where(users.c.user_name == user.user_name)
    existed_user = await database.fetch_one(query)
    if existed_user is not None:
        return Message(status=0, data=[], msg="username already exists")

    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    query = users.insert().values(user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                                  password=hashed.decode(), email_address=user.email_address, institution=user.institution,
                                  country=user.country)
    last_record_id = await database.execute(query)
    return Message(status=1, data=[{**user.dict(), "id": last_record_id}], msg="success")


@router.post("/users/login", response_model=Message)
async def login_user(user: UserIn):
    pw = user.password
    query = users.select().where(users.c.user_name == user.user_name)
    user = database.fetch_one(query)[0]
    if user is None:
        pass
    if bcrypt.checkpw(bytearray(pw), bytearray(user.password)):
        return ""
    else:
        pass
