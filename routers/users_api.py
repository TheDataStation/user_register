import sqlite3

from fastapi import APIRouter
from models.users import UserRegister, UserLogin, User
from models.message import Message
import bcrypt
import database_pb2
import database_pb2_grpc
import grpc

router = APIRouter()

channel = grpc.insecure_channel('localhost:50051')
stub = database_pb2_grpc.DatabaseStub(channel)


@router.get("/users/", response_model=Message)
async def get_all_users():
    resp = stub.GetAllUsers(database_pb2.User(limit=10))
    if resp.status == -1:
        return Message(status=0, data=[], msg="no existing users")
    return Message(status=1, data=get_users(resp.data), msg="success")


@router.post("/users/user_name", response_model=Message)
async def get_user_by_user_name(user_name: str):
    resp = stub.GetUserByUserName(database_pb2.User(user_name=user_name))
    if resp.status == -1:
        return Message(status=0, data=[], msg="user does not exist")
    return Message(status=1, data=[get_first_user(resp.data)], msg="success")


@router.post("/users/", response_model=Message)
async def create_user(user: UserRegister):
    # check if there is an existing user
    existed_user = stub.GetUserByUserName(database_pb2.User(user_name=user.user_name))
    if existed_user.status == 1:
        return Message(status=0, data=[], msg="username already exists")
    # no existing username, create new user
    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    new_user = database_pb2.User(user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                                 password=hashed.decode(), email=user.email, institution=user.institution,
                                 country=user.country)
    resp = stub.CreateUser(new_user)
    if resp.status == -1:
        return Message(status=0, data=[], msg="internal database error")
    return Message(status=1, data=[get_first_user(resp.data)], msg="success")


@router.post("/users/login", response_model=Message)
async def login_user(user: UserLogin):
    pw = user.password
    resp = stub.GetUserByUserName(database_pb2.User(user_name=user.user_name))

    if resp.status == -1:
        # username is wrong, login fail
        return Message(status=0, data=[], msg="username or password incorrect")
    user = get_first_user(resp.data, password=True)
    if bcrypt.checkpw(pw.encode(), user.password.encode()):
        user.password = ""  # never return password to the front end
        return Message(status=1, data=[user], msg="success")
    else:
        return Message(status=0, data=[], msg="username or password incorrect")


def get_first_user(data, password=False):
    for user in data:
        if password:
            return User(id=user.id, user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                        password=user.password, email=user.email, institution=user.institution, country=user.country)
        else:
            return User(id=user.id, user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                        password="", email=user.email, institution=user.institution, country=user.country)


def get_users(data):
    res = []
    for user in data:
        res.append(User(id=user.id, user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                        password="", email=user.email, institution=user.institution, country=user.country))
    return res
