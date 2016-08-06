import sqlalchemy as sa
conn = sa.create_engine('sqlite:///zoo.db')
print conn
conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)''')
