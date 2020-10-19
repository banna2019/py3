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
import json
from datetime import datetime
import time



st=time.strftime("%Y-%m-%d",time.localtime())
print(st)


try:
    for line in open("config.txt",'r',encoding='utf-8'):
        line = line.strip().split(',')
        cred = credential.Credential("xxxxxx", "xxxxxx")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "billing.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = billing_client.BillingClient(cred,"ap-hongkong", clientProfile)
        # client = billing_client.BillingClient(cred, "", clientProfile)

        req = models.DescribeAccountBalanceRequest()
        params = '{}'
        req.from_json_string(params)
        resp = client.DescribeAccountBalance(req)
        print(resp.to_json_string())

        messg=resp.to_json_string()
        jmsg=json.loads(messg)
        for key, value in jmsg.items():
            if key == 'Balance':
                print(type(value))

except TencentCloudSDKException as err:
    print(err)
