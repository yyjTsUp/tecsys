import unittest
from Common import logger

import requests


class BaseCase(unittest.TestCase):
    @classmethod
    def request(cls, method: str, url, params=None, data=None, json=None, **args):
        """
        自定义发送的请求
        :param method:请求方法
        :param url:请求url
        :param params:请求参数
        :param data:body
        :param json:json
        :param args:其他字典参数
        :return:res
        """
        method = method.upper()
        if method == "GET":
            res = requests.get(url, params=params, **args)
            res_de=res.text.encode('utf-8').decode('unicode_escape')
            logger.info(f'请求方法：{method},请求url：{url},服务器返回结果：{res_de}')
            return res
        elif method == 'POST':
            res = requests.post(url, data=data, json=json, **args)
            res_de=res.text.encode('utf-8').decode('unicode_escape')
            logger.info(f'请求方法：{method}，请求url：{url}，服务器返回结果：{res_de}')
            return res
