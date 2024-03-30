# author:yyj time:2024/3/29
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from selenium.webdriver.common.by import By
from env.config import data
from common.basepage import BasePage


class MainPage(BasePage):

    def login_page(self):
        self.driver.get(data['env']['prod']['webpage'])
        self.driver.find_element(By.XPATH,'//*[@id="Login"]').click()

if __name__ == '__main__':
    m=MainPage()
    m.login_page()
