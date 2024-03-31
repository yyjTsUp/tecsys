# author:yyj time:2024/3/30
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from business.loginpage import LoginPage


def test_login():
    login_page = LoginPage()
    login_page.driver.get('https://accounts.wondershare.cn/web/login_cn')
    # 页面操作
    login_page.click_passwd_login()
    login_page.enter_username('15827700311')
    login_page.enter_passwd('yj19940814')
    login_page.click_private_btn()
    login_page.click_login()
    # 断言
    assert login_page.driver.title =='帐号中心'
