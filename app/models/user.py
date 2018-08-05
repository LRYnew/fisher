# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 10:23
# @Author  : YJob
from sqlalchemy import Column, String, Integer, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.base import Base
from app import login_manager


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(24), unique=True, nullable=False)
    phone_number = Column(String(18), unique=True)
    wx_name = Column(String(32))
    wx_open_id = Column(String(50))
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    _password = Column('password', String(200), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def checked_password(self, raw):
        return check_password_hash(self._password, raw)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
