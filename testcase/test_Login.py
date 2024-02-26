import json
import unittest
from Common import login
from Common.basecase import BaseCase


class TestLogin(BaseCase):
    # 登陆-成功
    def test_login(self):
        resp = login.Login("auto", "sdfsdfsdf")
        res = json.loads(resp) #转成dict
        assert res["retcode"] == 0


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
