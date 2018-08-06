# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 10:42
# @Author  : YJob
from flask import current_app

from app import db
from app.libs.httper import HTTP
from app.models.book import Book


class YuShuBook(object):
    """
    鱼书 api
    """
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__full_single(result)
        self.__save_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PRE_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__full_collection(result)
        self.__save_collection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PRE_PAGE']

    def __full_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __full_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def __save_single(self, data):
        if not Book.query.filter_by(isbn=data['isbn']).first():
            book = Book()
            book.set_attr(data)
            db.session.add(book)
            db.session.commit()

    def __save_collection(self, data):
        for book in data['books']:
            self.__save_single(book)

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
