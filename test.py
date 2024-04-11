# author:yyj time:2024/3/27
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import pytest
import time

from selenium.webdriver.common.by import By

from common.driver import wdriver

driver=wdriver()
driver.get('https://www.12306.cn/index/')
driver.find_element(By.ID,'train_date').clear()
driver.find_element(By.ID,'train_date').send_keys('2024-04-11')
time.sleep(3)



