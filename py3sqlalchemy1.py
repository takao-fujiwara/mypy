import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
# print conn

conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)''')


ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)

rows = conn.execute('SELECT * FROM zoo')
print rows
