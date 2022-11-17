from flask import Flask
from flask import request
import const

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            return request.form['a']
        else:
            return request.form['b']
    except KeyError:
        return 'KeyError'


if __name__ == '__main__':
    app.run(debug=True)
