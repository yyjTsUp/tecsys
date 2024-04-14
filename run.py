# author:yyj time:2024/3/27
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import pytest
from notify import dingding
if __name__ == '__main__':
    pytest.main(['testcases'])
    dingding.DingTalkSendMag().push_message()
