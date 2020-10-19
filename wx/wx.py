#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/25 0025 20:25
# software: PyCharm



from wxpy import *


def login():
    """扫码登录"""
    bot = Bot()
    my_friend = bot.friends().search('',sex=MALE,city='上海')[0]
    my_friend.send('Hello WeChat!')
    my_friend.send_image('my_picture.jpg')

