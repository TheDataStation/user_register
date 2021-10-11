import grpc

import database_pb2
import database_pb2_grpc

import user_register_pb2
import user_register_pb2_grpc

from concurrent import futures
import bcrypt

channel = grpc.insecure_channel('localhost:50051')
database_service_stub = database_pb2_grpc.DatabaseStub(channel)

class UserRegisterServicer(user_register_pb2_grpc.UserRegisterServicer):
    def CreateUser(self, request: user_register_pb2.User, context):
        # check if there is an existing user
        existed_user = database_service_stub.GetUserByUserName(database_pb2.User(user_name=request.user_name))
        if existed_user.status == 1:
            # return Message(status=0, data=[], msg="username already exists")
            return user_register_pb2.UserResponse(status=1, msg="username already exists")
        # no existing username, create new user
        hashed = bcrypt.hashpw(request.password.encode(), bcrypt.gensalt())
        new_user = database_pb2.User(user_name=request.user_name, first_name=request.first_name, last_name=request.last_name,
                                     password=hashed.decode(), email=request.email, institution=request.institution,
                                     country=request.country)
        resp = database_service_stub.CreateUser(new_user)
        if resp.status == -1:
            # return Message(status=0, data=[], msg="internal database error")
            return user_register_pb2.UserResponse(status=1, msg="internal database error")

        # return Message(status=1, data=[get_first_user(resp.data)], msg="success")
        return user_register_pb2.UserResponse(status=0, msg="success")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_register_pb2_grpc.add_UserRegisterServicer_to_server(
        UserRegisterServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
