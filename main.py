from fastapi import FastAPI

from db_config import database, metadata, engine

from routers import users_api

metadata.create_all(engine)

app = FastAPI()

app.include_router(users_api.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def root():
    return {"message": "Welcome to user register"}
