# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 9:30
# @Author  : YJob

from flask import Blueprint

# 单蓝图 拆分多模块， 避免在 __init__ 内循环引用
web = Blueprint('web', __name__)
