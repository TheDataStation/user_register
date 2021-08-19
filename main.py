from fastapi import FastAPI

from routers import users_api

app = FastAPI()

app.include_router(users_api.router)


@app.get('/')
async def root():
    return {"message": "Welcome to user register"}
