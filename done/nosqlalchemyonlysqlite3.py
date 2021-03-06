import sqlite3
conn = sqlite3.connect('enterprise.db')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'

curs = conn.cursor()
curs.execute(ins, ('duck', 5, 0.0))
curs.execute(ins, ('bear', 2, 1000.0))
curs.execute(ins, ('weasel', 1, 2000.0))

curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()
