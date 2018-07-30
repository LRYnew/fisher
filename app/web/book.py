# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 16:47
# @Author  : YJob
import json
from flask import jsonify, request, render_template

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollectionViewModel
from app.web.web import web
from app.forms.book import SearchForm


@web.route('/search')
def search():
    """
    :q keyword or isbn
    :page 分页
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        books = BookCollectionViewModel()
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            # 面向过程
            # result = yushu_book.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.full(yushu_book, q)

        return json.dumps(books, default=lambda obj: obj.__dict__)
        # jsonify 序列化方法
        # return jsonify(books)
    else:
        # return jsonify({"msg": "参数验证失败"})
        return jsonify(form.errors)


@web.route('/test')
def test():
    r = {
        "name": "WJob",
        "age": 28
    }
    r1 = {
        "name": "ZJob",
        "age": 36
    }

    return render_template('test.html', r=r, r1=r1)
