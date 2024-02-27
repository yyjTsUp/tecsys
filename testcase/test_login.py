import json
import unittest
from Common import login
from Common.basecase import BaseCase
from ddt import ddt,data,unpack,file_data
@ddt
class TestLogin(BaseCase):
    # 登陆-成功
    @file_data("../testdata/logindata.json")
    def test_login(self,name,password,retcode):
        resp = login.Login(name, password)
        res = json.loads(resp) #转成dict
        assert res["retcode"] == retcode