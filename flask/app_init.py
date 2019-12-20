from flask import Flask, render_template
from flask import request
from flask import redirect

app = Flask(__name__)

info = [{'name': 'tom', 'gender': 'male', 'chinese': 90, 'math': 78},
        {'name': 'bob', 'gender': 'male', 'chinese': 87, 'math': 65},
        {'name': 'lucy', 'gender': 'female', 'chinese': 74, 'math': 73},
        {'name': 'lily', 'gender': 'female', 'chinese': 86, 'math': 90},
        {'name': 'alex', 'gender': 'male', 'chinese': 91, 'math': 77},
        {'name': 'john', 'gender': 'male', 'chinese': 79, 'math': 72},
        {'name': 'jeck', 'gender': 'male', 'chinese': 60, 'math': 99},
        {'name': 'tomas', 'gender': 'male', 'chinese': 88, 'math': 98},
        {'name': 'eva', 'gender': 'female', 'chinese': 100, 'math': 85},
        {'name': 'ella', 'gender': 'female', 'chinese': 70, 'math': 81}]


@app.route('/usr_info')
def usr_info():
    order_info = sorted(info, key=lambda score: eval(str(score['chinese']) + str(score['math'])), reverse=True)
    return render_template('usr_info_2.html', info=info, order=order_info[0:3])


@app.route('/change_info', methods=('GET', 'POST'))
def change_info():
    if request.method == 'GET':
        name = request.args['name']
        for p in info:
            if p['name'] == name:
                return render_template('change_info.html', usr=p)
    elif request.method == 'POST':
        for p in info:
            name = request.form['name']
            if p['name'] == name:
                p['gender'] = request.form['gender']
                p['chinese'] = request.form['chinese']
                p['math'] = request.form['math']
                return redirect('/usr_info')
    else:
        return '请求方法错误'


if __name__ == '__main__':
    app.run()
