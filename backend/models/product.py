from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

products = Table(
    'products', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('price'),
    Column('description', String),
    Column('id_restaurant', Integer),
)
