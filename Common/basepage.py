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
from common.driver import comdriver
import conftest


class BasePage:

    def __init__(self, mydriver=None):
        """
        判断：实例化对象如果指定driver，则用指定的driver;没有指定传值，则用common包里面的driver
        用途：执行用例的时候，pytest默认从conftest.py的fixture找driver，使得所有用例用一个driver实例
        :param options:
        :param mydriver:
        """
        if mydriver is None:
            self.driver =comdriver()
        else:
            self.driver=mydriver

    def wait_element(self, by, element):
        '''
        元素显示等待
        :by:八大元素定位方式
        ：element:页面元素
        :return: 单个元素对象
        '''
        try:

            element = WebDriverWait(self.driver, timeout=10).until(
                exp.element_to_be_clickable(
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
            logger.info(f"元素定位成功：{element}")
            return r
        except Exception as e:

            logger.error(traceback.format_exc())

    def find_elements(self, by, element):
        '''
        用于查找元素
        :param by: 元素定位方法
        :param element:
        :return:
        '''
        try:

            r = self.driver.find_elements(by, element)
            logger.info(f"元素定位成功：{element}")
            return r
        except Exception as e:

            logger.error(traceback.format_exc())


if __name__ == '__main__':
    m = BasePage()
    m.driver.get('https://www.imyfone.cn/')
    ele = m.find_element(By.ID, "Login")
    m.driver.get('https://www.baidu.com/')
    time.sleep(3)
