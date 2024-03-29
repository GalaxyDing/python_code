#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from flask_script import Manager
from app import app
from app import db
from app import Student

manager = Manager(app)


@manager.command
def init_databases():
    db.create_all()


@manager.command
def init_data():
    tom = Student(name='tom', gender='male', chinese=90, math=78)
    bob = Student(name='bob', gender='male', chinese=87, math=65)
    lucy = Student(name='lucy', gender='female', chinese=74, math=73)
    lily = Student(name='lily', gender='female', chinese=86, math=90)
    alex = Student(name='alex', gender='male', chinese=91, math=77)
    john = Student(name='john', gender='male', chinese=79, math=72)
    jeck = Student(name='jeck', gender='male', chinese=60, math=99)
    tomas = Student(name='tomas', gender='male', chinese=88, math=98)
    eva = Student(name='eva', gender='female', chinese=100, math=85)
    ella = Student(name='ella', gender='female', chinese=70, math=81)

    db.session.add_all([tom, bob, lucy, lily, alex, john, jeck, tomas, eva, ella])

    db.session.commit()


if __name__ == '__main__':
    manager.run()
