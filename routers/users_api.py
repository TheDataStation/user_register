import sqlite3

from fastapi import APIRouter
from db_config import database
from models.users import UserIn, users
from models.message import Message
import bcrypt

router = APIRouter()


@router.get("/users/", response_model=Message)
async def get_all_users():
    query = users.select()
    all_users = await database.fetch_all(query)
    return Message(status=1, data=all_users, msg="success")


@router.post("/users/user_name", response_model=Message)
async def get_user_by_user_name(username: str):
    query = users.select().where(users.c.user_name == username)
    user = await database.fetch_one(query)
    if user is None:
        return Message(status=0, data=[], msg="user does not exist")
    return Message(status=1, data=[user], msg="success")


@router.post("/users/", response_model=Message)
async def create_user(user: UserIn):
    # check if there is an existing user
    query = users.select().where(users.c.user_name == user.user_name)
    existed_user = await database.fetch_one(query)
    if existed_user is not None:
        return Message(status=0, data=[], msg="username already exists")
    # no existing username, create new user
    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    query = users.insert().values(user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                                  password=hashed.decode(), email_address=user.email_address, institution=user.institution,
                                  country=user.country)
    try:
        # let database integrity constraint double check the request
        last_record_id = await database.execute(query)
    except sqlite3.DatabaseError as err:
        return Message(status=0, data=[], msg="internal database error")
    return Message(status=1, data=[{**user.dict(), "id": last_record_id}], msg="success")


@router.post("/users/login", response_model=Message)
async def login_user(user: UserIn):
    pw = user.password
    query = users.select().where(users.c.user_name == user.user_name)
    user = await database.fetch_one(query)

    if user is None:
        # username is wrong, login fail
        return Message(status=0, data=[], msg="username or password incorrect")
    if bcrypt.checkpw(pw.encode(), user.password.encode()):
        return Message(status=1, data=[user], msg="success")
    else:
        return Message(status=0, data=[], msg="username or password incorrect")
