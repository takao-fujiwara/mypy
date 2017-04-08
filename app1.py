# coding: UTF-8

from datetime import datetime

import bottle
from bottle import get, post, run
from bottle import request, template, redirect
from bottle import HTTPError

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy import Unicode, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base

from bottle.ext import sqlalchemy

from wtforms.form import Form
from wtforms import validators
from wtforms import StringField, IntegerField, TextAreaField

Base = declarative_base()
engine = create_engine('sqlite://', echo=True)

plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

bottle.install(plugin)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(100), nullable=False)
    price = Column(Integer, nullable=False)
    memo = Column(UnicodeText)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<Book({},{},{},{})>'.format(
            self.title, self.price, self.memo, self.created_at)


class BookForm(Form):
    title = StringField(
        u'タイトル', [validators.required(
            message=u'入力して下さい'),
            validators.length(
            min=1, max=100,
            message=u'100文字以下で入力して下さい')]
    )

    price = IntegerField(
        u'価格', [validators.required(
            message=u'100文字以下で入力して下さい')]
    )

    name = TextAreaField(
        u'メモ', [validators.required(
            message=u'入力して下さい')]
    )


@get('/')
def top(db):
    redirect('/books')


@get('/books')
def index(db):
    books = db.query(Book).all()
    return template('index', books=books, request=request)


@get('/books/add')
def new(db):
    form = BookForm()
    return template('add', form=form, request=request)


@post('/books/add')
def create(db):
    form = BookForm(request.forms.decode())
    if form.validate():
        book = Book(
            title=form.title.data,
            price=form.price.data,
            memo=form.memo.data
        )

        db.add(book)
        redirect('/books')
    else:
        return template('edit', form=form, request=request)

@get('/books/<id:int>/edit')
def edit(db,id):

    form = BookForm()
    return template('edit', book=book, form=form, request=request)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
