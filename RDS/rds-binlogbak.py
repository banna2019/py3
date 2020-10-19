#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/23 0023 7:59
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


MY_COMMAND='/bin/mysql'
BACKUP_BIN='/bin/mysqlbinlog'
LOCAL_BACKUP_DIR='/data/backup'
BACKUP_LOG='/data/logs'
LOGSNAME='baklog.logs'
REMOTE_HOST='banna-mysql.ccrj65bnfxba.ap-southeast-1.rds.amazonaws.com'
REMOTE_PORT=3306
SERVER_ID=20003306
REMOTE_USER='root'
REMOTE_PASS='27jq7bhfO81B6qqNZfx6jK0R'
SLEEP_SECONDS=10




def binlog_file():
    # 创建必要的目录
    if not os.path.exists(LOCAL_BACKUP_DIR):
        os.makedirs(LOCAL_BACKUP_DIR)
    if not os.path.exists(BACKUP_LOG):
        os.makedirs(BACKUP_LOG)

    os.chdir(LOCAL_BACKUP_DIR)

    count = 0
    while i <= 2:
        FIRST_BINLOG=os.open(${MY_COMMAND} --host=${REMOTE_HOST} --user=${REMOTE_USER} --password=${REMOTE_PASS} -e 'show binary logs' 2>/dev/null | grep -v "Log_name" | awk '{print $1}' | head -n 1)
        if 



def send_mail(a):
    msg_from = 'banna@sixthnet.com'
    passwd = 'lvO3UI2mi-TM'
    msg_to = ['banna@sixthnet.com']
    # msg_to = ['banna@sixthnet.com','simon@sixthnet.com','admin@sixthnet.com']

    subject = REMOTE_HOST+"二进制日志文件备份失败"
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