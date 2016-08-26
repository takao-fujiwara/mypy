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

for post in query.all():
    print post.title

post = query.get(1)
# print post.title, post.text
print "<Post(title='%s', text='%s')>" % (post.title, post.text)

post = query.filter(Post.title == u'title_2').first()
# print post.title, post.text
print "<Post(title='%s', text='%s')>" % (post.title, post.text)
