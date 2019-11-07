from flask import Flask
from flask import render_template
from src.read_qa import read_qa
from flask import request
from flask import jsonify, json

qa_path = 'qa_source/qa.txt'
app = Flask(__name__)

user_name = None
user_id = None
choice = [3, 2, 2]


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
    # print(user_name)
    singal_dict, double_dict, fill_dict = read_qa(qa_path, choice=choice)
    # print(singal_dict)
    # print(double_dict)
    # print(fill_dict)
    # TODO
    from collections import defaultdict
    fill_list_dict = defaultdict(list)
    for key in fill_dict.keys():
        # print(fill_dict[key])
        i = 0
        left_index = 0
        right_index = 0
        current = 0
        split_fill = []
        for substr in fill_dict[key]:
            # print(substr)

            if '(' == substr or '（' == substr:
                left_index = i
                # print(left_index)
            if ')' == substr or '）' == substr:
                right_index = i
                if right_index - left_index == 1:
                    split_fill.append(fill_dict[key][current:left_index])
                    current = right_index + 1
                else:
                    left_index = 0
                    right_index = 0

            i = i + 1
        split_fill.append(fill_dict[key][current:])
        fill_list_dict[key].extend(split_fill)
    print(fill_list_dict)

    qa = {
        'user_name': user_name,
        'user_id': user_id
    }
    return render_template('question.html', qa=qa,
                           singal_dict=singal_dict,
                           double_dict=double_dict,
                           fill_dict=fill_list_dict)


@app.route('/check', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        rec_data = request.form.get('key')
        data = json.loads(rec_data)
        print(type(data))

    return jsonify({'ok': True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
