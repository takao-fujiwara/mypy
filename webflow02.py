from flask import Flask

app = Flask(__name__)


@app.route('/python15h')
def hello_python15h():
    return 'Welcom python15h!!'


if __name__ == '__main__':
    app.run()
