from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./user.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_name", sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("email_address", sqlalchemy.String),
    sqlalchemy.Column("institution", sqlalchemy.String),
    sqlalchemy.Column("country", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class User(BaseModel):
    id: int
    user_name: str
    first_name: str
    last_name: str
    password: str
    email_address: str
    institution: str
    country: str


class UserIn(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    password: str
    email_address: str
    institution: str
    country: str


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users/", response_model=List[User])
async def get_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                                  password=user.password, email_address=user.email_address, institution=user.institution,
                                  country=user.country)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}
