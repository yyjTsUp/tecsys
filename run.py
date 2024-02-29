# author:yyj time:2024/2/29
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import os.path
from datetime import datetime
import pytest

def get_reports():
    # 创建测试报告目录
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
    if not os.path.exists(reports_dir):
        os.mkdir(reports_dir)
    # -s:显示用例中的输出
    # -v:输出更详细的用例执行信息
    # __file__:本文件
    # 生成YYYY-MM-DD-HHMMSS格式时间戳
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d-%H%M%S")
    # 生成  --allure生成了报告原始.json文件,放在time_str.xml文件夹内
    pytest.main(['testcase/test_login.py', '-vs', '--alluredir',f'./reports/{time_str}xml'])
    #此处命令allure generate 将前面生成的json文件转换成html的报告
    os.system(f"allure generate ./reports/{time_str}xml -o ./reports/{time_str}html --clean-alluredir=./reports")
    #生成的报告index.html不能直接用chrome打开，需要用allure open选然后才能有样式和内容
    os.system(f"allure open ./reports/{time_str}html")

if __name__ == '__main__':
    get_reports()
