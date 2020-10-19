#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/20 0020 11:20
# software: PyCharm


from aliyunsdkcore import client
from aliyunsdkbssopenapi.request.v20171214 import QueryAccountBalanceRequest
from aliyunsdkcore.profile import region_provider
import sys, json
import smtplib
from email.mime.text import MIMEText
import time
from datetime import datetime



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
        print('%s的账户额度信息: ' % (zhm))
        for key, value in volist.items():
            # print(key,    value)
            if key == 'AvailableAmount':
                amount=value
                # print(amount)
                print('    可用额度: %s 单位: 人民币' % (value))
            elif key == 'AvailableCashAmount':
                camount=value
                # print(camount)
                print('    现金余额: %s 单位: 人民币' % (value))
        print('-----------------')
        dt = datetime.now()
        tm = dt.strftime('%x')
        print(tm)
        send_mail(tm,zhm,phone,amount,camount)


def send_mail(tm,zhm,phone,amount,camount):
    msg_from = 'bill@sixthnet.com'
    passwd = 'xxxxxx'
    msg_to = "xxxx@sixthnet.com"
    # msg_to = "xxxx@sixthnet.com,xxxx@sixthnet.com,xxxx@sixthnet.com"

    subject = "阿里云账户余额信息"
    content = ("查询日期: %s  %s的账户额度信息: 手机尾号: %s 可用额度: %s(人民币) 现金余额: %s(人民币)  可用余额和现金余额低于3000(人民币)请及时充值 谢谢!" % (tm,zhm,phone,amount,camount))

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    try:
        s = smtplib.SMTP_SSL("smtp.mail.us-east-1.awsapps.com",465)
        # s = smtplib.SMTP("smtp.mail.us-east-1.awsapps.com",465)
        s.login(msg_from,passwd)
        s.sendmail(msg_from,msg_to,msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        s.quit()


if __name__ == "__main__":
    check_money()
