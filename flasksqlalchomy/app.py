from flask import Flask, render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

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
    return render_template('usr_info_2.html', info=student)


if __name__ == '__main__':
    app.run()
