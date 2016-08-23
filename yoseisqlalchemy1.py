import sqlalchemy as sa
engine = sa.create_engine('sqlite:///post.db', echo=True)
# print engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
