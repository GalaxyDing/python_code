#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from app import app
from app import db
from app import DUser
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def init_data():
    tom = DUser(name='tom', gender='male', password='123456')
    bob = DUser(name='bob', gender='male', password='123456')
    lucy = DUser(name='lucy', gender='female', password='123456')
    lily = DUser(name='lily', gender='female', password='123456')
    alex = DUser(name='alex', gender='male', password='123456')
    john = DUser(name='john', gender='male', password='123456')
    jack = DUser(name='jack', gender='male', password='123456')
    tomas = DUser(name='tomas', gender='male', password='123456')
    eva = DUser(name='eva', gender='female', password='123456')
    ella = DUser(name='ella', gender='female', password='123456')

    db.session.add_all([tom, bob, lucy, lily, alex, john, jack, tomas, eva, ella])
    db.session.commit()


if __name__ == '__main__':
    manager.run()