# author:yyj time:2024/3/29
# -*- coding: utf-8 -*-
# coding=utf-8
import time
from selenium.webdriver.common.by import By
from common.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self):
        # 调用父类的构造函数
        super().__init__()
        #页面元素
        self.passwd_login_btn=(By.ID,'tab-password')
        self.email=(By.NAME,'email')
        self.passwd=(By.NAME,'password')
        self.login_btn=(By.NAME,"Next_Login")
        self.private_btn=(By.XPATH,"//*[@class='icon-svg_checkout-off icon-size']")

    def enter_username(self,username):
        #输入用户名
        self.find_element(*self.email).click()
        self.find_element(*self.email).send_keys(username)
    def enter_passwd(self,passwd):
        #输入密码
        self.find_element(*self.passwd).click()
        self.find_element(*self.passwd).send_keys(passwd)

    def click_login(self):
        #点击登陆按钮
        self.find_element(*self.login_btn).click()

    def click_private_btn(self):
        self.wait_element(*self.private_btn)
        self.find_element(*self.private_btn).click()
    def click_passwd_login(self):
        self.find_element(*self.passwd_login_btn).click()

if __name__ == '__main__':
    T=LoginPage()
    T.driver.get('https://accounts.wondershare.cn/web/login_cn')
    T.click_passwd_login()
    T.click_private_btn()
    time.sleep(3)




