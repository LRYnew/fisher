# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 21:41
# @Author  : YJob


def is_isbn_or_key(work):
    """
    判断参数 为关键字或者isbn编码
    :param work:
    :return:
    """
    isbn_or_key = 'key'
    if len(work) == 13 and work.isdigit():
        isbn_or_key = 'isbn'
    shor_work = work.replace('-', '')
    if '-' in work and len(shor_work) == 10 and shor_work.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
