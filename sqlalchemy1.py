from sqlalchemy import create_engine


engine = create_engine('sqlite:///memory:', echo=True)
print engine


from sqlalchemy.ext import declarative
Base = declarative.declarative_base()
from sqlalchemy import Column, Integer, Unicode, UnicodeText


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    text = Column(UnicodeText)

    def __repr__(self):
        return "<Post(title='%s',text='%s')>" % (self.title, self.text)


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

post = Post(title=u'title_1', text=u'first')
session.add(post)
session.commit()
session.add_all([
    Post(title=u'title_2', text=u'second'),
    Post(title=u'title_3', text=u'third'),
])
session.commit()

query = session.query(Post)

for post in query.all():
    print post.title

post = query.get(1)
print post.title
