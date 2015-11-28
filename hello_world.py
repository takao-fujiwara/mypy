# coding: utf-8

from bottle import route, run, template


@route('/hellox')
def hellox():
    return template('Hello {{string}}', string='testworld')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
