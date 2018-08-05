# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 21:41
# @Author  : YJob

class BookViewModel(object):
    """
    书籍 单本 view model
    """
    def __init__(self, data):
        self.title = data["title"]
        self.author = "、".join(data["author"])
        self.pages = data["pages"]
        self.price = data["price"]
        self.publisher = data["publisher"]
        self.summary = data["summary"]
        self.image = data["image"]
        self.isbn = data["isbn"]
        self.pubdate = data["pubdate"],
        self.binding = data["binding"]

    @property
    def intro(self):
        intro = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return ' / '.join(intro)

class BookCollectionViewModel(object):
    """
    书籍 集合 view model
    """
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def full(self, data, keyword):
        self.total = data.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in data.books]


class _BookViewModel(object):
    """
    面向过程编程
    书籍 view model
    """

    @classmethod
    def package_single(cls, data, keyword):
        resulted = {
            "total": 0,
            "keyword": keyword,
            "books": []
        }

        if data:
            resulted["total"] = 1
            resulted['books'] = [cls.__cut_book_data(data)]

        return resulted

    @classmethod
    def package_collection(cls, data, keyword):
        resulted = {
            "total": 0,
            "keyword": keyword,
            "books": []
        }

        if data:
            resulted["total"] = 1
            resulted['books'] = [cls.__cut_book_data(book) for book in data["books"]]

        return resulted

    @staticmethod
    def __cut_book_data(data):
        book = {
            "title": data["title"],
            "author": "、".join(data["author"]),
            "pages": data["pages"],
            "price": data["price"],
            "publisher": data["publisher"],
            "summary": data["summary"],
            "image": data["image"]
        }

        return book
