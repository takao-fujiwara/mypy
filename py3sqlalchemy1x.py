import sqlalchemy as sa
conn = sa.create_engine('sqlite:///memory:', echo=True)
print(conn)
