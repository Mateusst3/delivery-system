from fastapi import APIRouter
from config.db import engine
from models.index import users
from schemas.index import User

user = APIRouter()


@user.get("/")
async def read_data():
    # return conn.excecute(users.select()).fetchall()
    return engine.connect().execute(users.select()).fetchall()


@user.get("/{id}")
async def read_data(id: int):
    # return engine.connect().excecute(users.select().where(users.c.id == id)).fetchall()
    return engine.connect().execute(users.select().where(users.c.id == id)).fetchall()


@user.post("/")
async def write_data(user: User):
    engine.connect().execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    return engine.connect().execute(users.select()).fetchall()


@user.put("/{id}")
async def update_data(id: int, user: User):
    engine.connect().execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return engine.connect().excecute(users.select()).fetchall()


@user.delete("/")
async def delete_data(id: int):
    engine.connect().execute(users.delete().where(users.c.id == id))
    return engine.connect().execute(users.select()).fetchall()
    # engine.connect().execute(users.delete().where(users.c.id == id))
    # return engine.connect().excecute(users.select()).fetchall()
