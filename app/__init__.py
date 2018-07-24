# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 16:47
# @Author  : YJob
from flask import Flask
from app.models.book import db


def create_app():
    """
    初始化app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.web import web
    app.register_blueprint(web)
