# coding: utf-8

from bottle import route, get, run, template, request, static_file


@get('/upload')
def upload():
    return template('upindex')


@route('/upload', method='POST')
def do_upload():
    title = request.forms.title
    memo = request.forms.memo
    upload = request.files.get('upload', '')
    if upload:
        if not upload.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return 'File extension not allowed!'
        else:
            save_path = get_save_path()
            upload.save(save_path, overwrite=True)
            return 'title=%s memo=%s filename=%s' % (title, memo, upload.filename)
    else:
        return 'title=%s memo=%s' % (title, memo)


def get_save_path():
    path_dir = "./static/img/"
    return path_dir


# この下の/static/の部分は実際のパスでなくても任意の名前で可#
#  例 ↓ /file/ でアクセス#
@route('/static/<filename:path>')
def show_static(filename):
    return static_file(filename, root="./static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
