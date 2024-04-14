# author:yyj time:2024/3/29
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from env.config import data


class MainPage(BasePage):

    def __init__(self,mydriver=None):
        super().__init__(mydriver)
        self.driver.get(data["env"]["prod"]["mainpage"])
        # 页面元素
        self.product_btn = (By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[1]/nav')
        self.function_btn = (By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[2]/nav')
        self.vip_btn = (By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[3]/nav')
        self.artle_btn = (By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[4]/nav')
        self.helpcenter_btn = (By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[5]/nav')
        self.sub_pro_btns = (By.CLASS_NAME, 'ml-2 font-weight-bold font-size-large')
        self.sub_pro_computerProfess_btn = (
        By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[1]/div/div/div/div/div/div[1]/div/div/div/a')
        self.sub_func_edit = (
        By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[2]/div/div/div/div/div/div[1]/div/nav/h5/a')
        self.sub_vip_signal = (
        By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[3]/div/div/div/div/div/div[1]/div/h6/a')
        self.sub_artle_baselesson = (
        By.XPATH, '/html/body/header/nav[2]/div/div/div[2]/ul/li[4]/div/div[1]/div/div/div/div[1]/div/nav/h5')
        self.download_btn = (By.XPATH, '/html/body/main/section[1]/div[2]/div/a[1]')


    def click_product_btn(self):
        self.find_element(*self.product_btn).click()

    def click_sub_pro_computer(self):
        self.wait_element(*self.sub_pro_computerProfess_btn).click()

    def click_personalvip_btn(self):
        self.find_element(*self.sub_vip_signal).click()

    def move_and_download(self):
        download_btn = self.find_element(*self.download_btn)
        actions = ActionChains(self.driver)
        actions.move_to_element(download_btn)
        actions.perform()
        download_btn.click()


    def alert_win(self):
        alert = self.driver.switch_to.alert
        print('alert text', alert.text)
        # 接受通知
        alert.accept()
        # 不接受通知
        # alert.dismiss()


if __name__ == '__main__':
    m = MainPage()
    m.click_product_btn()
