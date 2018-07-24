# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 16:47
# @Author  : YJob
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.web.web import web
from app.forms.book import SearchForm


@web.route('/search')
def search():
    """
    :param q: 关键字 or isbn
    :param page: 分页
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        yushu_book = YuShuBook()
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            result = yushu_book.search_by_isbn(q)
        else:
            result = yushu_book.search_by_keyword(q, page)
        # jsonify 序列化方法
        return jsonify(result)
    else:
        # return jsonify({"msg": "参数验证失败"})
        return jsonify(form.errors)
