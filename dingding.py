# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:work liu
@file: dingding
@time: 2020/9/4   9:16
@IDE:PyCharm
"""

import json
import requests

def message(link=1):
    url="https://oapi.dingtalk.com/robot/send?access_token=c4b0f985a4b84a8fa99784a6b9c59c8e0f12477d52458434a1570a101438f30b"
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('尊敬的各位你好,你的测试报告已好,请查收')
        },
        "at":{
            "atMobiles":[
                "13137111812"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True     #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()