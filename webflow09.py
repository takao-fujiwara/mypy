# webflow09.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('webflow09.html')

if __name__ == '__main__':
    app.run(debug=True)
