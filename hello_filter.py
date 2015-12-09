# coding: utf-8

from bottle import route, run, template


@route('/versions/<no:float>')
def versions(no):
    return template('versions={{no}}', no=no)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
