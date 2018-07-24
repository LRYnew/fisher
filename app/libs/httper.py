# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 22:21
# @Author  : YJob

import requests


# 爬虫: scrapy 框架 or requests + beautiful soap
class HTTP:
    """
    HTTP 类
    """
    @staticmethod
    def get(url, return_json=True):
        """
        get 方法
        :param url: url 请求
        :param return_json: 是否返回 json 格式
        :return:
        """
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
