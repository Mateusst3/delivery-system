from fastapi import FastAPI
from routes.index import user, restaurant, product

app = FastAPI()

app.include_router(user)
app.include_router(restaurant)
app.include_router(product)
