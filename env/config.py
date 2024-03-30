# author:yyj time:2024/3/30
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
'''
读取yaml文件
return:data dict type
'''
import os.path
import yaml

conf_yml =os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.yml')
with open(conf_yml,encoding='utf-8') as f:
    data=yaml.safe_load(f)
