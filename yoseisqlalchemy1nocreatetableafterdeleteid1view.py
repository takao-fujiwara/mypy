# coding: UTF-8

import sqlalchemy as sa
conn = sa.create_engine('sqlite:///post.db', echo=True)
print conn
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Post(Base):
        __tablename__ = 'posts'
        id = sa.Column(sa.Integer, primary_key=True)
        title = sa.Column(sa.Unicode(255), nullable=False)
        text = sa.Column(sa.UnicodeText)

        def __rep__(self):
            return
            "<Post(title='%s', text='%s')>" % (self.title, self.text)


# Base.metadata.create_all(conn)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

query = session.query(Post)
# データの削除
# post = query.get(1)
# session.delete(post)
# session.commit()

# データの更新
post = query.get(2)
post.text = u"second2"
session.commit()

# id = 1 は既に削除されていることを確認
# id = 2 は　text が更新されていることを確認
# 削除、更新後のテーブルの表示

for post in query.all():
        print post.title, post.text
