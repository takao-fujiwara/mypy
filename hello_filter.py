# coding: utf-8

from bottle import route, run, template


@route('/versions/<no:float>')
def versions(no):
    return template('versions={{no}}', no=no)


@route('/article/<id:int>')
def article(id):
    return template('article={{id}}', id=id)


@route('/greeting/<name>')
def greeting(name):
    return template('Hello {{name}}', name=name)


@route('/hello')
def hello():
    return template('Hello {{string}}', string='world')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
