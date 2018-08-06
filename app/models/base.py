# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 10:23
# @Author  : YJob
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    """
    基础类
    """
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attr(self, attr_dict):
        """
        循环动态赋值
        :param attr_dict:
        :return:
        """
        for key, val in attr_dict.items():
            if hasattr(self, key) and key != 'id':
                if isinstance(val, list):
                    val = '、'.join(val)
                setattr(self, key, val)
