#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/22 0022 14:14
# software: PyCharm

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.billing.v20180709 import billing_client, models
import sys,json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
from datetime import datetime



st=time.strftime("%Y-%m-%d",time.localtime())
print(st)

mslist=[]

def check_money():
    for line in open("config.txt", 'r', encoding='utf-8'):
        line = line.strip().split(',')
        zhm = line[0]
        phone = line[1]
        accessKey = line[2]
        accessSecret = line[3]
        region = line[4]
        cred = credential.Credential(accessKey, accessSecret)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "billing.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = billing_client.BillingClient(cred, region, clientProfile)
        req = models.DescribeAccountBalanceRequest()
        params = '{}'
        req.from_json_string(params)
        resp = client.DescribeAccountBalance(req)
        messg = resp.Balance
        ye = messg / 100
        mssg = ('{0}({1}): {2}(余额)'.format(zhm, phone, ye))
        mslist.append(mssg)
    a=print_mail(mslist)
    send_mail(a)
    print(a)




def print_mail(mslist):
    b = ''
    for i in mslist:
        b += i + '\n\n'
    return  b

def send_mail(a):
    msg_from = 'xxxxx@sixthnet.com'
    passwd = 'xxxxx'
    # msg_to = ['xxxx@sixthnet.com']
    msg_to = ['xxxxx@sixthnet.com','xxxx@sixthnet.com','admin@sixthnet.com']

    subject = "腾讯云账户余额信息"+st
    content = (a)

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = ','.join(msg_to)

    try:
        s = smtplib.SMTP_SSL("smtp.mail.us-east-1.awsapps.com",465)
        s.login(msg_from,passwd)
        s.sendmail(msg_from, msg['To'].split(','), msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        s.quit()


if __name__ == '__main__':
    check_money()
