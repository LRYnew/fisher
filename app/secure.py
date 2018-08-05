# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 12:26
# @Author  : YJob
import datetime

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
SECRET_KEY = 'C3EimXgFEL9Zi5VRuJeCuWzZIrIujgKn'
REMEMBER_COOKIE_DURATION = datetime.timedelta(weeks=1)