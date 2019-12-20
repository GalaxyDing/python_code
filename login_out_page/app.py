import os
from flask import Flask
from flask import request
from flask import session
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@39.105.87.164/py1907'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
# os.urandom(10)
app.secret_key = '\xf1\x1c\x16\xa1\xa8\xc6\xee\xc1\x84'


class DUser(db.Model):
    __tablename__ = 'usr_info'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(32), default='000000')


@app.route('/')
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        usr_name = request.form.get('name')
        password = request.form.get('password')
        usr = DUser.query.filter_by(name=usr_name, password=password).first()
        if usr is None:
            return redirect('/register')
        else:
            session['uid'] = usr.id
            return redirect('/show')

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
        new_name = request.form.get('name')
        new_usr = DUser(name=new_name, gender=request.form.get('gender'), password=request.form.get('password'))
        db.session.add(new_usr)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('uid')
    return redirect('/')


if __name__ == '__main__':
    app.run()
