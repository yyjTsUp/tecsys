# author:yyj time:2024/4/11
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import pytest
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 全局变量
testdata = {"driver": ""}
imageinfo = {"file_path": ""}


@pytest.fixture(scope='session', autouse=True)
def wdriver():
    # 定义PC浏览器的驱动
    root_dir = os.path.dirname(os.path.abspath(__file__))
    driverpath = os.path.join(root_dir, './driver/chromedriver.exe')
    s = Service(driverpath)
    driver = webdriver.Chrome(service=s)
    # 设置driver全局隐式等待最长5s
    testdata["driver"] = driver
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

@pytest.fixture(scope='session', autouse=True)
def opts_wdriver():
    # 定义要下载文件的PC浏览器的驱动
    root_dir = os.path.dirname(os.path.abspath(__file__))
    driverpath = os.path.join(root_dir, './driver/chromedriver.exe')
    s = Service(driverpath)
    prefs = {
        "download.default_directory": r"C:\Software\yangyj\TecSys\download_files",
        "profile.default_content_setting_values.automatic_downloads": 1,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    # option=options
    # # 绕过https安全隐私
    # # option.add_argument('--ignore-ssl-errors=yes')
    # # option.add_argument('--ignore-certificate-errors')
    # driver = webdriver.Chrome(service=s, options=option)
    # 设置driver全局隐式等待最长5s
    testdata["driver"] = driver
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver


# 截图操作，每个用例执行之后都要操作，有需要再移除注释
# @pytest.fixture(scope='function', autouse=True)
# def get_screenshot(wdriver):
#     import os
#     outcome = yield
#     report = outcome.get_result()
#     # 创建截图文件夹
#     screenshotsfile = os.path.join(os.path.dirname(__file__), 'screenshots')
#     if not os.path.exists(screenshotsfile):
#         os.mkdir(screenshotsfile)
#     #设置图片名称
#     picturename = report.nodeid.replace("/", '_').replace("::", "_").replace(".py", "_").split("[")[0]
#     # pngfilename = os.path.join(screenshots, f'{time.strftime("%Y_%m_%d_%H_%M_%S_")}{time.monotonic_ns()}.png')
#     #设置截图文件路径
#     pngfilename = os.path.join(screenshotsfile, picturename)
#     #截图操作
#     wdriver.save_screenshot(pngfilename)

def screenshot(filename):
    # 创建截图文件夹
    screenshotsfile = os.path.join(os.path.dirname(__file__), 'screenshots')
    if not os.path.exists(screenshotsfile):
        os.mkdir(screenshotsfile)
    pngfilename = os.path.join(screenshotsfile, filename)
    imageinfo["file_path"] = pngfilename
    testdata["driver"].save_screenshot(pngfilename)


'''
hookimpl装饰器表明函数是回调函数，在用例各个阶段都会触发；
item参数记录用例运行阶段各个对象
1、判断用例阶段为call且运行失败
2、取出driver对象进行截图
'''


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    out = yield
    report = out.get_result()
    extra = getattr(report, "extras", [])
    if report.when == 'call' and report.failed:
        # 开始截图，拼接图片名称
        picturename = report.nodeid.replace("/", '_').replace("::", "_").replace(".py", "_").split("[")[0]
        screenshot(f'{picturename}.png')
        extra.append(pytest_html.extras.image(imageinfo["file_path"]))
        report.extras = extra
