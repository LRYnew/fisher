# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 16:47
# @Author  : YJob
from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    """
    初始化app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.web import web
    app.register_blueprint(web)
