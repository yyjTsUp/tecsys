import json
from const import consts
from Common.basecase import BaseCase


# 登陆，获取token
def Login(username, pwd):
    url = consts.domain + '/api/mgr/loginReq'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"  # data=dict
        # "application/json"                       #data=str
    }
    # data="username={}&password={}".format(username,pwd)
    data = {
        "username": username,
        "password": pwd
    }
    # 使用封装好的request方法
    resp = BaseCase.request('post', url=url, headers=headers, data=data)
    res=resp.text
    # res=resp.headers['Set-Cookie']
    return res


if __name__ == "__main__":
    print(Login('autoer', 'sdfsdfsdf'))
