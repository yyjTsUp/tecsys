# author:yyj time:2024/4/12
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import os.path
import json

def read_report():
    print(os.path.dirname(os.path.abspath(__file__)))
    conf_json =os.path.join(os.path.dirname(os.path.abspath(__file__)),'report.json')
    with open(conf_json,encoding='utf-8') as f:
        data=json.load(f)
        return data

if __name__ == '__main__':
    print(read_report())