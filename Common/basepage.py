# author:yyj time:2024/3/30
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
'''
所有页面的基类
'''
import time
import traceback

from selenium.webdriver.common.by import By

from common.logger import logger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import Select

from common.driver import wdriver


class BasePage:

    def __init__(self):
        # 获取driver
        self.driver = wdriver()

    def wait_element(self, by, element):
        '''
        元素显示等待
        :by:八大元素定位方式
        ：element:页面元素
        :return: 单个元素对象
        '''
        try:

            element = WebDriverWait(self.driver, timeout=10).until(
                exp.presence_of_element_located(
                    (by, element)
                )
            )
            logger.debug(f"元素定位成功：{element}")
            return element

        except Exception as e:
            logger.error(traceback.format_exc())

    def wait_elements(self, by, element):
        '''
        元素显示等待
        :by:八大元素定位方式
        ：element:页面元素
        :return: 返回多个对象
        '''
        try:

            element = WebDriverWait(self.driver, timeout=10).until(
                exp.presence_of_all_elements_located(
                    (by, element)
                )
            )
            logger.debug(f"元素定位成功：{element}")
            return element

        except Exception as e:
            logger.error(traceback.format_exc())

    def find_element(self, by, element):
        '''
        用于查找元素
        :param by: 元素定位方法
        :param element:
        :return:
        '''
        try:

            r = self.driver.find_element(by, element)
            logger.debug(f"元素定位成功：{element}")
            return r
        except Exception as e:
            logger.error(traceback.format_exc())


if __name__ == '__main__':
    m = BasePage()
    m.driver.get('https://www.baidu.com/')
    ele = m.find_element(By.CLASS_NAME, "hot-refresh-text")
    ele.click()
    time.sleep(3)