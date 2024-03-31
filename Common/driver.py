# author:yyj time:2024/3/28
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
def wdriver(options=None):
    # 定义PC浏览器的驱动
    root_dir = os.path.dirname(os.path.abspath(__file__))
    driverpath = os.path.join(root_dir, '../driver/chromedriver.exe')
    s = Service(driverpath)
    if options:
        wdriver = webdriver.Chrome(service=s,options=options)
    else:
        wdriver = webdriver.Chrome(service=s)
        #设置driver全局隐式等待最长5s
    wdriver.implicitly_wait(5)
    wdriver.maximize_window()
    return wdriver
