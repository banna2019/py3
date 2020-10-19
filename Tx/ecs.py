#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/25 0025 21:44
# software: PyCharm


from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    cred = credential.Credential("AKIDnZDJEuP498Svii9Gcq5BewxoPzbnnZnp", "5B1NI0saAWfnuqfaFtOk992e5Hd0D9oL")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "cvm.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cvm_client.CvmClient(cred, "ap-hongkong", clientProfile)

    req = models.DescribeRegionsRequest()
    params = '{}'
    req.from_json_string(params)

    resp = client.DescribeRegions(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)