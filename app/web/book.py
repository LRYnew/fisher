# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 16:47
# @Author  : YJob
import json
from flask import jsonify, request, render_template, flash

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollectionViewModel, BookViewModel
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
    books = BookCollectionViewModel()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            # 面向过程
            # result = yushu_book.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.full(yushu_book, q)

        # 对象进行序列化
        # return json.dumps(books, default=lambda obj: obj.__dict__)
        # jsonify 序列化方法
        # return jsonify(books)
    else:
        # return jsonify({"msg": "参数验证失败"})
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新进行搜索')

    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail', endpoint='book_detail')
def detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)

    book = BookViewModel(yushu_book.first)

    return render_template('book_detail.html',book=book,gifts=[],wishes=[])


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
