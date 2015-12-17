# coding: utf-8
# test
from bottle import route, run, template, request


@route('/show_header')
def show_header():
    headers_list = ["<p> %s = %s <p>" % (k, v)
                    for k, v in request.headers.items()]
    return "".join(headers_list)


@route('/search/<keyword:re:[a-z]+>')
def search(keyword):
    return template('keyword={{keyword}}', keyword=keyword)


@route('/photo/<image_path:path>')
def photo(image_path):
    return template('image_path={{image_path}}', image_path=image_path)


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
