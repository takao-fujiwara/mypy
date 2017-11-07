# coding: utf-8

from bottle import route, get, post, run, template, request, response


@post('/show_file')
def show_file():
    upload = request.files.get('upload')
    return template('name={{name}}', name=upload.filename)


@post('/show_form')
def show_form():
    keyandvalue_list = ["<p> %s = %s </p>" % (k, v)
                        for k, v in request.forms.items()]
    return "".join(keyandvalue_list)


@post('/show_kfname')
def show_kfname():
    upload = request.files.get('upload').filename
    keyandvalue_list = ["%s = %s" % (k, v)
                        for k, v in request.forms.items()]
    kword = " ,  ".join(keyandvalue_list)
    kfname = upload + " , " + kword
    return template('filename={{kfname}}', kfname=kfname)


@get('/show_query')
def show_query():
    query_list = ["<p> %s = %s </p>" % (k, v)
                  for k, v in request.query.items()]
    return "".join(query_list)


@route('/show_header')
def show_header():
    headers_list = ["<p> %s = %s </p>" % (k, v)
                    for k, v in request.headers.items()]
    return "".join(headers_list)


@route('/show_cookie')
def show_cookie():
    count = int(request.cookies.get('counter', '0'))
    count += 1
    response.set_cookie('counter', str(count))
    return template('You visited this page {{count}} times', count=str(count))


@route('/search/<keyword:re:[a-z]+>')
def search(keyword):
    return template('keyword={{keyword}}', keyword=keyword)


@route('/photo/<image_path:path>')
def photo(image_path):
    return template('image_path={{image_path}}', image_path=image_path)


@route('/versions/<no:float>')
def versions(no):
    return template('versions={{no}}', no=no)


@route('/show/<id:int>')
def show(id):
    return template('rebase', id=id)


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
