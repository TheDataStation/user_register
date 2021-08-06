from pydantic import BaseModel
import sqlalchemy
from db_config import metadata


class User(BaseModel):
    id: int
    user_name: str
    first_name: str
    last_name: str
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


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_name", sqlalchemy.String, unique=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("email_address", sqlalchemy.String),
    sqlalchemy.Column("institution", sqlalchemy.String),
    sqlalchemy.Column("country", sqlalchemy.String),
)