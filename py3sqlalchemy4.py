import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()


class Zoo(Base):
        __tablename__ = 'zoo'
        critter = sa.Column('critter', sa.String, primary_key=True)
        count = sa.Column('count', sa.Integer)
        damages = sa.Column('damages', sa.Float)

        def __init__(self, critter, count, damages):
            self.critter = critter
            self.count = count
            self.damages = damages

        def __rep__(self):
            return
            "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

# Base.metadata.create_all(conn)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

forth = Zoo('d4', 4, 4000.0)
session.add(forth)
session.commit()
