#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/24 0024 22:15
# software: PyCharm


import requests,json,sys,os,datetime


webhook="https://oapi.dingtalk.com/robot/send?access_token=95a25d8b8f0945ecd0f0ac992f4be80d3f738ded0acb199ff356426e70fca675"
user=sys.argv[1]
text=sys.argv[3]
data={
    "msgtype": "text",
    "text": {
        "content": text
    },
    "at": {
        "atMobiles": [
            user
        ],
        "isAtAll": False
    }
}
headers = {'Content-Type': 'application/json'}
x=requests.post(url=webhook,data=json.dumps(data),headers=headers)
if os.path.exists("/usr/local/zabbix/logs/dingding.log"):
    f=open("/usr/local/zabbix/logs/dingding.log","a+")
else:
    f=open("/usr/local/zabbix/logs/dingding.log","w+")
f.write("\n"+"--"*30)
if x.json()["errcode"] == 0:
    f.write("\n"+str(datetime.datetime.now())+"    "+str(user)+"    "+"发送成功"+"\n"+str(text))
    f.close()
else:
    f.write("\n"+str(datetime.datetime.now()) + "    " + str(user) + "    " + "发送失败" + "\n" + str(text))
    f.close()