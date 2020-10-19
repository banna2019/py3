#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/22 0022 16:55
# software: PyCharm


from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.billing.v20180709 import billing_client, models
import json
from datetime import datetime
import time


mslist=[]

for line in open("config.txt", 'r', encoding='utf-8'):
    line = line.strip().split(',')
    zhm = line[0]
    phone = line[1]
    accessKey = line[2]
    accessSecret = line[3]
    region = line[4]
    # print(line)
    # print(zhm,accessKey,accessSecret,region)
    cred = credential.Credential(accessKey,accessSecret)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "billing.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = billing_client.BillingClient(cred,region, clientProfile)

    req = models.DescribeAccountBalanceRequest()
    params = '{}'
    req.from_json_string(params)
    resp = client.DescribeAccountBalance(req)
    # print(resp.to_json_string())

    messg = resp.Balance
    # print(type(messg))
    # print(messg)
    ye=messg/100
    # print(ye)
    mssg = ('{0}({1}): {2}(余额)'.format(zhm,phone,ye))
    print(mssg)
