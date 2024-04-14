# author:yyj time:2024/3/28
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import os
import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from business.miaopage import MainPage
from env.config import data


class TestMiaoPage:
    def test_top_navbar(self,wdriver):
        mainpage = MainPage(mydriver=wdriver)
        '''
        页面操作：
        1/点击顶部导航栏：产品
        2/点击下拉子菜单栏“电脑专业版”,跳转链接
        '''
        mainpage.click_product_btn()
        mainpage.click_sub_pro_computer()
        expurl = 'https://miao.wondershare.cn/product-2023.html'
        assert mainpage.driver.current_url == expurl




    def test_download_btn(self,opts_wdriver):
        # prefs = {
        #     "download.default_directory": r"C:\Software\yangyj\TecSys\download_files",
        #     "profile.default_content_setting_values.automatic_downloads": 1,
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True
        # }
        # chrome_options = Options()
        # chrome_options.add_experimental_option('prefs',prefs)
        mainpage = MainPage(mydriver=opts_wdriver)
        '''
        页面操作：
        1、设置下载路径
        2、鼠标移动到download按钮,悬停
        3、、点击下载
        '''
        mainpage.move_and_download()
        '''
        检查下载完成：
        1、每1s轮询下载文件夹，文件名是否存在
        2、获取到文件夹内文件名称，断言
        '''
        exp_filename = 'filmora_setup_full13770.exe'
        download_dir = 'C:\Software\yangyj\TecSys\download_files'
        while not os.path.isfile(os.path.join(download_dir, exp_filename)):
            print('等待下载文件')
            time.sleep(1)
        mainpage.driver.close()

        file_name = os.listdir('C:\Software\yangyj\TecSys\download_files')

        assert file_name[0] == exp_filename
