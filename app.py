from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/question')
def question():
    return render_template('question.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
