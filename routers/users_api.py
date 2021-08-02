from fastapi import APIRouter
from typing import List
from db_config import database
from models.users import User, UserIn, users

router = APIRouter()


# Todo: encrypt password when stored into database
@router.get("/users/", response_model=List[User])
async def get_all_users():
    query = users.select()
    return await database.fetch_all(query)


@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(user_name=user.user_name, first_name=user.first_name, last_name=user.last_name,
                                  password=user.password, email_address=user.email_address, institution=user.institution,
                                  country=user.country)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}
