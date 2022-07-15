from pydantic import BaseModel


class Products(BaseModel):
    name: str
    price: float
    description: str
    id_restaurant: int
