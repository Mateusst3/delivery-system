from fastapi import APIRouter
from config.db import engine
from models.index import restaurants
from schemas.index import Restaurants

restaurant = APIRouter()


@restaurant.get("/restaurants/")
async def get_restaurants():
    return engine.connect().execute(restaurants.select()).fetchall()


@restaurant.get("/restaurants/{id}")
async def read_restaurants(id: int):
    return engine.connect().execute(restaurants.select().where(restaurants.c.id == id)).fetchall()


@restaurant.post("/restaurants/")
async def register_restaurants(restaurant: Restaurants):
    engine.connect().execute(restaurants.insert().values(
        name=restaurant.name,
    ))
    return engine.connect().execute(restaurants.select()).fetchall()


@restaurant.put("/restaurants/{id}")
async def update_restaurants(id: int, restaurant: Restaurants):
    engine.connect().execute(restaurants.insert().values(
        name=restaurant.name,
    )).where(restaurants.c.id == id)
    return engine.connect().execute(restaurants.select()).fetchall()


@restaurant.delete("/restaurants/{id}")
async def delete_restaurants(id: int):
    engine.connect().execute(restaurants.delete().where(restaurants.c.id == id))
    return engine.connect().execute(restaurants.select()).fetchall()
