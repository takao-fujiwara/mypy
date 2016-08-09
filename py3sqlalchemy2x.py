import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
# print conn

meta = sa.MetaData()

# Flask8では E128のErroがでるが引数の位置を第一引数にそろえればＯＫ
# Erroがででも実行はＯＫ　　行整形の仕方の問題かも 以下のURL参照
# http://stackoverflow.com/questions/18497923/
# python-pep8-e128-indentation-error-how-can-this-by-styled

zoo = sa.Table('zoo', meta,
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
