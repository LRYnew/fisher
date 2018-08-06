# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 22:20
# @Author  : YJob
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from fisher import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:root@localhost:3306/fisher'

from app.models import db

migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
