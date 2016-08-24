import sqlalchemy as sa
conn = sa.create_engine('sqlite:///post.db', echo=True)
# print engine
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


Base.metadata.create_all(conn)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

post = Post(title=u'title_1', text=u'first')
session.add(post)
session.commit()

session.add_all([
    Post(title=u'title_2', text=u'second'),
    Post(title=u'title_3', text=u'third'),
    ])

session.commit()
