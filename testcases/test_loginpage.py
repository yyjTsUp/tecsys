# author:yyj time:2024/3/30
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from business.loginpage import LoginPage
from env.config import data


def test_login(wdriver):
    login_page = LoginPage(wdriver)
    login_page.driver.get(data["env"]["prod"]["loginpage"])
    '''
    页面操作：
    1/切换到密码登录
    2/输入账号密码
    3/同意隐私政策
    4/点击登录
    '''
    login_page.click_passwd_login()
    login_page.enter_username('15827700311')
    login_page.enter_passwd('yj19940814')
    login_page.click_private_btn()
    login_page.click_login()
    # 断言
    assert login_page.driver.title =='帐号中心'
