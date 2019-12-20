import os

from flask import Flask, render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

# 文件夹绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@39.105.87.164/py1907'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'student_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    chinese = db.Column(db.Float, default=0.0)
    math = db.Column(db.Float, default=0.0)


@app.route('/')
def student_info():
    student = Student.query.all()
    order_condition = db.desc(Student.chinese + Student.math)
    order_student = Student.query.order_by(order_condition).limit(5)
    return render_template('usr_info_2.html', info=student, order_s=order_student)


@app.route('/detail_info')
def detail_info():
    uid = int(request.args['uid'])
    detail = Student.query.get(uid)
    return render_template('detail_info.html', stu=detail)


@app.route('/change_info', methods=('GET', 'POST'))
def change_info():
    if request.method == 'GET':
        uid = int(request.args['uid'])
        p = Student.query.get(uid)
        return render_template('change_info.html', usr=p)
    elif request.method == 'POST':
        uid = int(request.form['uid'])
        p = Student.query.get(uid)
        p.gender = request.form['gender']
        p.chinese = request.form['chinese']
        p.math = request.form['math']

        upload_img = request.files['avatar']
        filepath = os.path.join(UPLOAD_DIR, p.name)
        upload_img.save(filepath)
        return redirect('/')
    else:
        return '请求方法错误'


if __name__ == '__main__':
    app.run()
