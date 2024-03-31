# author:yyj time:2024/3/29
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from env.config import data


class MainPage(BasePage):

    def mainfe(self):
        self.driver.get(data['env']['prod']['mainpage'])

if __name__ == '__main__':
    m=MainPage()
    m.login_page()
