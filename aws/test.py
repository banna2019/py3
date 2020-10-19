#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/5/22 0022 17:10
# software: PyCharm


import sys
import boto3
from boto3.session import Session
import configparser


def ec2_check():
    ec2 = boto3.resource('ec2')

    for instance in ec2.instances.all():
        # volume = ec2.Volume('id')
        # ID = instance(ec2.Instance())
        print(instance)
        # print(ID)


if __name__ == "__main__":
    print(ec2_check())