import json
import unittest

from Common.basecase import BaseCase
from business import Lession
from const import consts


class TestLession(BaseCase):
    def test_01_addlession(self):
        adddata = {
            "name": "大等数学",
            "desc": "大学基础课程",
            "display_idx": "1"
        }
        data = json.dumps(adddata)
        resp = Lession.add_lession(self, data)
        # 添加断言
        self.assertEqual(resp["retcode"], 0)

    def test_01_addlession(self):
        adddata = {
            "name": "大学开心高等数学",
            "desc": "大学基础课程",
            "display_idx": "1"
        }
        data =json.dumps(adddata)
        resp=Lession.add_lession(self,data)
        #添加断言
        self.assertEqual(resp["retcode"],0)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLession("test_01_addlession"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
