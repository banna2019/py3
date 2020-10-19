#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/5/8 0008 21:09
# software: PyCharm


import boto3


client = boto3.client('kafka')
response = client.describe_cluster(
    ClusterArn='string'
)

response = client.list_cluster(
    ClusterNameFileter='string',
    MaxResults=123,
    NextToken='string'
)



response = client.get_bootstrap_brokers(
    ClusterArn='string'
)
