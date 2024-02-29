"""
封装课程相关的功能接口
"""
import json
import random

from Common.basecase import BaseCase
from const import consts


class Lession():
    def add_lession(self,data):
        """
                添加课程
                :return:
                """
        url = consts.domain + '/api/mgr/sq_mgr/'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        adddata = {
            "action": "add_course",
            "data": data
        }
        resp = BaseCase.request(method='post', url=url, headers=headers, data=adddata)
        # 上下游传参：课程id
        res = json.loads(resp.text)
        consts.lession_id = res["id"]
        return res

    def list_lession(self):
        """
                课程列表
                :return:
        """
        url = consts.domain + '/api/mgr/sq_mgr/'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "action": "list_course",
            "pagenum": 1,
            "pagesize": 20
        }
        # 发送请求
        resp = BaseCase.request(method='get', url=url, headers=headers, params=params)
        return json.loads(resp.text)


if __name__ == '__main__':
    data="{\"name\": \"唐学数学\",\"desc\": \"大学基础课程\",\"display_idx\": \"1\"}"
    temp = Lession().add_lession(data)
    print(temp)
