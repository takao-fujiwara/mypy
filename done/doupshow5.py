# coding: utf-8

import os
from datetime import datetime

import bottle
from bottle import route, get, post, run, template, request
from bottle import static_file, redirect, url
from bottle import HTTPError


from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy import Unicode, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from wtforms.form import Form
from wtforms import validators
from wtforms import StringField, TextAreaField
Base = declarative_base()
engine = create_engine('sqlite:///mynote.db', echo=True)

plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

bottle.install(plugin)


class Mynote(Base):
    __tablename__ = 'mynotes'
    id = Column(Integer, primary_key=True)
    memo = Column(UnicodeText)
    title = Column(Unicode(100), nullable=False)
    fname = Column(Unicode(200), nullable=True)
    created_at = Column(DateTime, default=datetime.now)


def __repr__(self):
    return '<Mynote({},{},{},{})>'.format(
        self.memo, self.title, self.fname, self.created_at)


class MynoteForm(Form):
    title = StringField(
        u'タイトル', [validators.required(
            message=u'入力して下さい'),
            validators.length(
            min=1, max=100,
            message=u'100文字以下で入力して下さい')]
    )

    memo = TextAreaField(
        u'メモ', [validators.required(
            message=u'入力して下さい')]
    )

    fname = StringField(
        u'ファイル名', [validators.required(
            message=u'入力して下さい'),
            validators.length(
            min=1, max=100,
            message=u'100文字以下で入力して下さい')]
    )


@get('/')
def top(db):
    redirect('/mynotes')


@get('/mynotes')
def index(db):
    mynotes = db.query(Mynote).all()
    return template('indexmynote', mynotes=mynotes, request=request)


@get('/upload')
def upload():
    return template('upindex')


@route('/upload', method='POST')
def do_upload(db):
    # python2.7 windows用
    title = request.forms.getunicode('title')
    memo = request.forms.getunicode('memo')
    uploadfile = request.files.get('upload', '')
    if uploadfile:
        if not uploadfile.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return 'File extension not allowed!'
        else:
            save_path = get_save_path()
            uploadfile.save(save_path, overwrite=True)

            mynote = Mynote(
                title=title,
                memo=memo,
                fname=uploadfile.filename
            )
            db.add(mynote)
            redirect('/mynotes')
    else:
        mynote = Mynote(
            title=title,
            memo=memo,
            fname=''
        )
        db.add(mynote)
        redirect('/mynotes')


def get_save_path():
    path_dir = "./static/img/"
    return path_dir


# この下の/static/の部分は実際のパスでなくても任意の名前で可#
#  例 ↓ /file/ でアクセス#
@route('/static/<filename:path>', name='static_file')
def show_static(filename):
    return static_file(filename, root="./static")


@get('/mynotes/<id:int>/edit')
def edit(db, id):

    mynote = db.query(Mynote).get(id)
    if not mynote:
        return HTTPError(404, 'Mynote is not found.')
    form = MynoteForm(request.POST, mynote)

    return template('em', mynote=mynote, form=form, request=request, url=url)


@post('/mynotes/<id:int>/edit')
def update(db, id):

    mynote = db.query(Mynote).get(id)
    if not mynote:
        return HTTPError(404, 'Mynote is not found.')

    form = MynoteForm(request.forms.decode())

    if form.validate():
        mynote.title = form.title.data
        mynote.memo = form.memo.data
        mynote.fname = form.fname.data
        redirect('/mynotes')
    else:
        return template('em', form=form, request=request)


@post('/mynotes/<id:int>/delete')
def destroy(db, id):

    mynote = db.query(Mynote).get(id)
    if not mynote:
        return HTTPError(404, 'Mynote is not found.')

    if mynote.fname:
        delete_path = get_save_path()+mynote.fname
        os.remove(delete_path)

    db.delete(mynote)
    redirect('/mynotes')


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
