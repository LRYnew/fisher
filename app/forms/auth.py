# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 11:21
# @Author  : YJob
from wtforms import StringField, PasswordField, Form
from wtforms.validators import Length, DataRequired, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    """
    注册验证
    """
    email = StringField(
        validators=[DataRequired(message='邮箱不能为空'), Email('不符合邮箱填写规范'), Length(min=5, max=50, message="邮箱不能超过50个字符")])

    nickname = StringField(validators=[DataRequired(message='昵称不能为空'), Length(min=1, max=20, message='请填写1-20个字符内的昵称')])

    password = PasswordField(validators=[DataRequired('密码不能为空'), Length(6, 32, message='密码长度6-32')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('昵称已被注册')


class LoginForm(Form):
    """
    注册验证
    """
    email = StringField(
        validators=[DataRequired(message='邮箱不能为空'), Email('不符合邮箱填写规范'), Length(min=5, max=50, message="邮箱不能超过50个字符")])

    password = PasswordField(validators=[DataRequired('密码不能为空'), Length(6, 32, message='密码长度6-32')])
