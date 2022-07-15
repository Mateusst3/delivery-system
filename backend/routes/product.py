from fastapi import APIRouter
from config.db import engine
from models.index import products
from schemas.index import Products

product = APIRouter()


@product.get("/products/")
async def get_products():
    return engine.connect().execute(products.select()).fetchall()


@product.get("/restaurants/{id}/products/")
async def get_products_by_restaurant(id: int):
    return engine.connect().execute(products.select().where(products.c.id_restaurant == id)).fetchall()


@product.post("/restaurants/{id}/products/")
async def register_product_by_restaurant(id: int, product: Products):
    engine.connect().execute(products.insert().values(
        name=product.name,
        price=product.price,
        description=product.description,
        id_restaurant=product.id_restaurant,
    ))
    return engine.connect().execute(products.select().where(products.c.id_restaurant == id)).fetchall()
