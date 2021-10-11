import grpc

import database_pb2
import database_pb2_grpc

import user_register_pb2
import user_register_pb2_grpc
from models.users import User
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

from concurrent import futures
import bcrypt

channel = grpc.insecure_channel('localhost:50051')
database_service_stub = database_pb2_grpc.DatabaseStub(channel)

# Adding global variables to support access token generation
SECRET_KEY = "736bf9552516f9fa304078c9022cea2400a6808f02c02cdcbd4882b94e2cb260"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Helper function for server method LoginUser
def get_first_user(data, password=False):
    for user in data:
        if password:
            return User(id=0, user_name=user.user_name, first_name="", last_name="",
                        password=user.password, email="", institution="", country="")
        else:
            return User(id=0, user_name=user.user_name, first_name="", last_name="",
                        password="", email="", institution="", country="")


# The following function handles the creation of access tokens (for LoginUser)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


class UserRegisterServicer(user_register_pb2_grpc.UserRegisterServicer):

    def CreateUser(self, request: user_register_pb2.User, context):
        print("Create User")
        # check if there is an existing user
        existed_user = database_service_stub.GetUserByUserName(database_pb2.User(user_name=request.user_name))
        if existed_user.status == 1:
            return user_register_pb2.UserResponse(status=1, msg="username already exists")
        # no existing username, create new user
        hashed = bcrypt.hashpw(request.password.encode(), bcrypt.gensalt())
        new_user = database_pb2.User(user_name=request.user_name, first_name=request.first_name,
                                     last_name=request.last_name,
                                     password=hashed.decode(), email=request.email, institution=request.institution,
                                     country=request.country)
        resp = database_service_stub.CreateUser(new_user)
        if resp.status == -1:
            return user_register_pb2.UserResponse(status=1, msg="internal database error")

        return user_register_pb2.UserResponse(status=0, msg="success")

    def LoginUser(self, request, context):
        # check if there is an existing user
        existed_user = database_service_stub.GetUserByUserName(database_pb2.User(user_name=request.user_name))
        # First check if the user exists
        if existed_user == -1:
            return user_register_pb2.TokenResponse(status=1, token="username is wrong")
        user = get_first_user(existed_user.data, password=True)
        if bcrypt.checkpw(request.password.encode(), user.password.encode()):
            # In here the password matches, we store the content for the token in the message
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user.user_name}, expires_delta=access_token_expires
            )
            return user_register_pb2.TokenResponse(status=0, token=str(access_token))
        user_register_pb2.TokenResponse(status=1, token="password does not match")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_register_pb2_grpc.add_UserRegisterServicer_to_server(
        UserRegisterServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
