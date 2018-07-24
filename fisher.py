# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 22:29
# @Author  : YJob
from app import create_app

app = create_app()

if __name__ == '__main__':
    # 如果该模块作为主入口文件，执行下列语句
    # 生产环境 ngnix + uwsgi，不调用flask自己的服务启动，本模块不是主入口模块，不应该执行以下语句。
    app.run(host='0.0.0.0', port=7077, debug=app.config['DEBUG'])
