#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/21 0021 10:28
# software: PyCharm


from aliyunsdkcore import client
from aliyunsdkbssopenapi.request.v20171214 import QueryAccountBalanceRequest
from aliyunsdkcore.profile import region_provider
import sys, json
import smtplib
from email.mime.text import MIMEText
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
                my_open.write('    可用额度: %s 单位: 人民币' % (value) + "\n")
            elif key == 'AvailableCashAmount':
                camount=value
                # print(camount)
                # print('    现金余额: %s 单位: 人民币' % (value))
                my_open.write('    现金余额: %s 单位: 人民币' % (value)+ "\n")
        print('------------------------------------')
    my_open.close()



if __name__ == '__main__':
    check_money()