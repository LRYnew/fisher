# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 21:23
# @Author  : YJob
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    """
    书籍模型
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    author = Column(String(10), default='未知')
    binding = Column(String(10))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer, default=0)
    pubdate = Column(String(20))
    isbn = Column(String(20), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(100))

    def sample(self):
        pass