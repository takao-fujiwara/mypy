# coding: utf-8

from bottle import route, get, post, run, template, request, static_file


@post('/show_kfname')
def show_kfname():
    upload = request.files.get('upload').filename
    keyandvalue_list = ["%s = %s" % (k, v)
                        for k, v in request.forms.items()]
    kword = " ,  ".join(keyandvalue_list)
    kfname = upload + " , " + kword
    return template('filename={{kfname}}', kfname=kfname)


@get('/upload')
def upload():
    return template('upindex')


@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('upload', '')
    if not upload.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return 'File extension not allowed!'
    save_path = get_save_path()
    upload.save(save_path, overwrite=True)
    return 'Upload OK. FilePath: %s%s' % (save_path, upload.filename)


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
