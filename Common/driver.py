# author:yyj time:2024/3/28
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service


def comdriver():
    # 定义PC浏览器的驱动
    root_dir = os.path.dirname(os.path.abspath(__file__))
    driverpath = os.path.join(root_dir, '../driver/chromedriver.exe')
    s = Service(driverpath)
    driver = webdriver.Chrome(service=s)
    # 设置driver全局隐式等待最长5s
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver
