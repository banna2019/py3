#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/24 0024 10:15
# software: PyCharm

import os,sys
import time
import logging
import sys,json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
from datetime import datetime
import pymysql


MY_COMMAND='/bin/mysql'
BACKUP_BIN='/bin/mysqlbinlog'
LOCAL_BACKUP_DIR='/data/backup'
BACKUP_LOG='/data/logs'
LOGSNAME='baklog.logs'
SLEEP_SECONDS=10

# SERVER_ID= number+port

def check_config():
    for line in open("D:\Coding\py3\RDS\config.json",'r',encoding='utf-8'):
        # print(line)
        line = line.strip().split(',')
        number=line[0]
        # print(number)
        name=line[1]
        # print(name)
        hostname=line[2]
        # print(hostname)
        user=line[3]
        # print(user)
        passwd=line[4]
        # print(passwd)
        port=line[5]
        # print(port)

        i = 0
        while True:
            con =pymysql.connect(hostname=hostname,port=port,user=user,password=passwd,db='banna_mysql',charset='utf-8')
            cur = con.cursor()
            flog = cur.execute('show binary logs')
            print(flog)
            i +=1
            if i == 3:
                break


if __name__ == '__main__':
    check_config()