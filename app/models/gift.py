# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 10:23
# @Author  : YJob
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationships

from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(20), nullable=False)
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
