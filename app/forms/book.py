# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 11:29
# @Author  : YJob
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    """
    搜索参数验证
    """
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
