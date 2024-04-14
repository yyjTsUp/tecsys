# author:yyj time:2024/4/12
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
# author:yyj time:2024/4/10
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
import requests
from testdata import config as report_summary


class DingTalkSendMag:
    """发送钉钉通知"""

    def __init__(self):
        report_dict = report_summary.read_report()
        self.case_num = report_dict["summary"]["total"]
        self.passed_num = report_dict["summary"]["passed"]
        if "failed" in report_dict["summary"] :
            self.failed_num = report_dict["summary"]["failed"]
        else:
            self.failed_num = 0
        if "skipped" in report_dict["summary"]:
            self.skipped_num = report_dict["summary"]["skipped"]
        else:
            self.skipped_num = 0
        # 集成jenkins后，用jenkins上的链接
        self.report_url = 'file:///C:/Users/ybfyyj1994/PycharmProjects/pythonProject1/report.html?sort=result'
        self.duration = round(report_dict["duration"], 2)

    def push_message(self):
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=d8b4e8d87ac4ec45643dc81301740f9f80a3d0607b0125d826864b34a67a3970"
        content = {
            "msgtype": "text",
            "text": {
                "content": "web自动化脚本执行结果：\n运行总数:" + str(self.case_num)
                           + "\n通过数量：" + str(self.passed_num)
                           + "\n失败数量：" + str(self.failed_num)
                           + "\n跳过数量：" + str(self.skipped_num)
                           # + "\n构建地址：\n" + self.job_url
                           + f"\n执行用例时长：{self.duration}s"
                           + "\n报告地址：" + self.report_url
            }

        }
        response = requests.post(url=webhook, json=content, verify=False)
        if response.json()['errmsg'] != "OK":
            return response.text
        return response


if __name__ == '__main__':
    DingTalkSendMag().push_message()
