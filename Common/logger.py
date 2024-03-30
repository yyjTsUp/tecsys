# author:yyj time:2024/3/30
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
"""
自定义日志工具：
1.控制台输入日志
2.运行日志记录到文件中
"""
import logging
import os.path

logger = logging.getLogger('web auto')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")

sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)
# 添加控制台输出
logger.addHandler(sh)

# 定义日志存放路径
logs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs')
if not os.path.exists(logs):
    os.mkdir(logs)
logfile = os.path.join(logs, 'web_auto.log')
fh = logging.FileHandler(logfile)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)

if __name__ == '__main__':
    logger.info("this is test for web auto")
    logger.error('this is error')