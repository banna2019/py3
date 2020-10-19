#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/20 0020 15:12
# software: PyCharm


from aliyunsdkcore import client
from aliyunsdkbssopenapi.request.v20171214 import QueryAccountBalanceRequest
from aliyunsdkcore.profile import region_provider
import sys, json

import smtplib
from email.mime.text import MIMEText
import time
from datetime import datetime


import pandas as pd
# from datetime import datetime
#
# dt=datetime.now()
# tm=dt.strftime('%x')
# print(tm)

# file=open('config.txt','r')
# for line in file.readlines():
#     line=line.strip().split(',')
#     zhm=line[0]
#     accessKey=line[1]
#     accessSecret=line[2]
#     region=line[3]
#     # print(line)
#     print(zhm,accessKey,accessSecret,region)


# for line in open("config.txt"):
#     line = line.strip().split(',')
#     # print(line)
#     zhm=line[0]
#     phon=line[1]
#     accessKey=line[2]
#     accessSecret=line[3]
#     region=line[4]
#     print(zhm,phon,accessKey,accessSecret,region)


# clt = client.AcsClient('xxxx','xxxx','cn-hongkong')
# clt = client.AcsClient('xxxx','xxxx','cn-hongkong')
# request = QueryAccountBalanceRequest.QueryAccountBalanceRequest()
# request.set_accept_format("JSON")
# result = clt.do_action_with_exception(request)
# mesjs = json.loads(result)
# volist = mesjs['Data']
# print(volist)



# def send_mail():
#     msg_from = 'xxxx@sixthnet.com'
#     passwd = 'xxxxxx'
#     msg_to = "xxxxxx@sixthnet.com,xxxxxx@sixthnet.com,admin@sixthnet.com"
#
#     # msg_from = 'xxxxxx0@163.com'
#     # passwd = 'xxxxxx'
#     # msg_to = "xxxxxx@qq.com"
#
#     subject = "阿里云账户余额信息"
#     content = ("hello world!")
#
#     msg = MIMEText(content)
#     msg['Subject'] = subject
#     msg['From'] = msg_from
#     msg['To'] = msg_to
#
#     try:
#         # s = smtplib.SMTP("smtp.163.com",25)
#         s = smtplib.SMTP_SSL("smtp.mail.us-east-1.awsapps.com",465)
#         # s = smtplib.SMTP("smtp.mail.us-east-1.awsapps.com",465)
#         s.login(msg_from,passwd)
#         s.sendmail(msg_from,msg_to,msg.as_string())
#         print("发送成功")
#     except smtplib.SMTPException as e:
#         print(e)
#     finally:
#         s.quit()
#
#
# if __name__ == '__main__':
#     send_mail()


st=time.strftime("%Y-%m-%d",time.localtime())
print(st)
