import os
from flask import Blueprint
from flask import Flask
from flask import request
from flask import session
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dll:123456@182.92.241.192/some'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://atao:123456@atao.run/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
# os.urandom(10)
app.secret_key = '\xf1\x1c\x16\xa1\xa8\xc6\xee\xc1\x84'


class DUser(db.Model):
    __tablename__ = 'usr_info'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(32), default='000000')
    article = db.Column(db.TEXT, default='')


@app.route('/')
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        usr_name = request.form.get('username')
        password = request.form.get('password')
        usr = DUser.query.filter_by(name=usr_name, password=password).first()
        if usr is None:
            return redirect('/register')
        else:
            session['uid'] = usr.id
            return redirect('/index')

    else:
        return render_template('login.html')


@app.route('/show')
def show_info():
    uid = session.get('uid')
    if uid is None:
        return redirect('/register')
    else:
        user = DUser.query.get(uid)
        return render_template('show.html', usr=user)


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        pw = request.form.get('password')
        re_pw = request.form.get('rePassword')
        new_name = request.form.get('username')
        if pw == re_pw:
            new_usr = DUser(name=new_name, password=request.form.get('password'))
            db.session.add(new_usr)
            db.session.commit()
            return redirect('/login')
        else:
            replay = '密码不一致请重新输入'
            return render_template('register.html', replay=replay)
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('uid')
    return redirect('/')


@app.route('/index')
def index():
    uid = session.get('uid')
    user = DUser.query.get(uid)
    if uid is None:
        return redirect('/login')
    else:
        return render_template('index.html', usr=user)


@app.route('/write', methods=('GET', 'POST'))
def write():
    uid = session.get('uid')
    user = DUser.query.get(uid)
    if uid is None:
        return redirect('/login')
    else:
        if request.method == 'POST':
            content = request.form.get('content')
            uid = request.form.get('uid')
            user = DUser.query.get(uid)
            user.article = content
            db.session.commit()
            return render_template('results.html')
        else:
            return render_template('write.html', usr=user)


if __name__ == '__main__':
    app.run()
