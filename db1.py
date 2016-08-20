from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


engine = create_engine('sqlite://', echo=True)
print engine

metadata = MetaData()
metadata.bind = engine

menus = Table(
    'menus', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('kcal', Integer)
)

from sqlalchemy.ext import declarative
Base = declarative.declarative_base()
