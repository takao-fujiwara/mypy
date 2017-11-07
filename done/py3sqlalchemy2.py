import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
# print conn

meta = sa.MetaData()

zoo = sa.Table('zoo',
               meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
               )

meta.create_all(conn)

conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
conn.execute(zoo.insert(('duck', 10, 0.0)))

result = conn.execute(zoo.select())

rows = result.fetchall()
print rows
