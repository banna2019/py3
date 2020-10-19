#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/20 0020 11:20
# software: PyCharm


from aliyunsdkcore import client
from aliyunsdkbssopenapi.request.v20171214 import QueryAccountBalanceRequest
from aliyunsdkcore.profile import region_provider
import sys,json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
from datetime import datetime


st=time.strftime("%Y-%m-%d",time.localtime())
# print(st)
mslist=[]

def check_money():
    for line in open("config.txt",'r',encoding='utf-8'):
        line = line.strip().split(',')
        # print(line)
        zhm=line[0]
        phone=line[1]
        accessKey=line[2]
        accessSecret=line[3]
        region=line[4]
        # print(zhm,accessKey,accessSecret,region)
        clt = client.AcsClient(accessKey,accessSecret,region)
        request = QueryAccountBalanceRequest.QueryAccountBalanceRequest()
        request.set_accept_format("JSON")
        result = clt.do_action_with_exception(request)
        mesjs = json.loads(result)
        volist = mesjs['Data']
        # print(volist)
        # print(st)
        for key, value in volist.items():
            if key == 'AvailableCashAmount':
                camount=value
                mssg=('{0}({1}): {2}(余额)'.format(zhm,phone,camount))
                # print(mssg)
        mslist.append(mssg)
    a = print_mail(mslist)
    send_mail(a)

def print_mail(mslist):
    b = ''
    for i in mslist:
        b += i + '\n\n'
    return  b

def send_mail(a):
    msg_from = 'bill@sixthnet.com'
    passwd = 'xxxx'
    # msg_to = ['xxxx@sixthnet.com']
    msg_to = ['xxxx@sixthnet.com','xxxx@sixthnet.com','admin@sixthnet.com']

    subject = "阿里云账户余额信息"+st
    content = (a)

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    # msg['To'] = msg_to
    msg['To'] = ','.join(msg_to)

    try:
        s = smtplib.SMTP_SSL("smtp.mail.us-east-1.awsapps.com",465)
        s.login(msg_from,passwd)
        # s.sendmail(msg_from,msg_to,msg.as_string())
        s.sendmail(msg_from, msg['To'].split(','), msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        s.quit()

if __name__ == "__main__":
    check_money()

