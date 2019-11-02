from flask import Flask
from flask import render_template
from src.read_qa import read_qa
from flask import request

qa_path = 'qa_source/qa.txt'
app = Flask(__name__)

user_name = None
user_id = None


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/question', methods = ['POST', 'GET'])
def question():
    # TODO
    global user_name
    global user_id
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_id = request.form['user_id']
    print(user_name)
    singal_dict, double_dict, fill_dict = read_qa(qa_path, choice = [2, 1, 1])
    # print(singal_dict)
    # print(double_dict)
    # print(fill_dict)
    qa = {
        'user_name': user_name,
        'user_id': user_id
    }
    return render_template('question.html', qa=qa,
                           singal_dict=singal_dict,
                           double_dict=double_dict,
                           fill_dict=fill_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
