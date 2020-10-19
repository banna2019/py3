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
print(st)


def check_money():
    my_open = open('feiyong'+st+'.txt', 'a', encoding='utf-8')
    my_open.write(st + "\n")
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
        print(st)
        print('%s的账户额度信息: ' % (zhm))
        my_open.write('{0}的账户额度信息: '.format(zhm)+"\n")
        for key, value in volist.items():
            # print(key,    value)
            if key == 'AvailableAmount':
                amount=value
                # print(amount)
                # print('    可用额度: %s 单位: 人民币' % (value))
                my_open.write('    可用额度: %s  单位:人民币' % (value) + "\n")
            elif key == 'AvailableCashAmount':
                camount=value
                # print(camount)
                # print('    现金余额: %s 单位: 人民币' % (value))
                my_open.write('    现金余额: %s  单位:人民币' % (value)+ "\n")
        print('------------------------------------')
    my_open.close()


def send_mail():
    msg_from = 'xxxxl@sixthnet.com'
    passwd = 'xxxxxx'
#    msg_to = "xxxx@sixthnet.com"
    msg_to = ['xxxx@163.com','xxxx@sixthnet.com','xxxx@sixthnet.com','admin@sixthnet.com']
    subject = "阿里云账户余额信息"+st
    # content = ("阿里云账户金额统计信息请查看附件!"+"\n""    备注: 可用余额和现金余额低于3000(人民币)请及时充值 谢谢!")

    msg = MIMEMultipart()
    # msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = ','.join(msg_to)
    #msg['To'] = msg_to

    msg.attach(MIMEText("阿里云账户金额统计信息请查看附件!"+"\n""    备注: 可用余额和现金余额低于3000(人民币)请及时充值 谢谢!","plain","utf-8"))

    att = MIMEText(open("feiyong"+st+".txt","rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment; filename='feiyong'+st+'.txt'"
    msg.attach(att)

    try:
        s = smtplib.SMTP_SSL("smtp.mail.us-east-1.awsapps.com",465)
        # s = smtplib.SMTP("smtp.mail.us-east-1.awsapps.com",465)
        s.login(msg_from,passwd)
        s.sendmail(msg_from,msg['To'].split(','),msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        s.quit()


if __name__ == "__main__":
    check_money()
    send_mail()
