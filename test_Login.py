import unittest
from Login import login
class TestLogin(unittest.TestCase):
    #登陆-成功
    def test_login(self):
        resp=login.Login("auto","sdfsdfsdf")
        print(resp)
        assert resp["retcode"]==0


if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))

    runner=unittest.TextTestRunner()
    runner.run(suite)
