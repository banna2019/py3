#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/5/23 0023 21:46
# software: PyCharm


import boto3


def main():
    ec2 = boto3.resource('ec2')  # 使用EC2服务
    instance = ec2.Instance('i-02090bd44364a17e5')  # 获取一个EC2实例（一台机器）
    state = instance.state  # 获取实例的当前状态，返回是一个字典
    '''
    state说明:
        0 : pending  		
        16 : running 		
        32 : shutting-down 	
        48 : terminated 	
        64 : stopping 		
        80 : stopped 		
    '''

    # 返回实例的一个或多个网络接口信息
    attrs = instance.network_interfaces_attribute

    # 返回实例的公有ip，每次重启后该ip会改变
    publicIp = instance.public_ip_address

    # 返回实例的私有ip，每次重启后该ip不会改变
    privateIp = instance.private_ip_address

    # 停止一个实例，返回一个字典对象
    stop_dic = instance.stop()

    # 等待一个实例完成停止操作
    instance.wait_until_stopped()

    # 启用一个实例，返回一个字典对象
    start_dic = instance.start()

    # 等待一个实例到它正常运行
    instance.wait_until_running()

    # 也可以选出正在运行的所有实例
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for instance in instances:
        print
        instance.id


if __name__ == '__main__':
    main()
