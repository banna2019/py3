#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/12 0012 22:47
# software: PyCharm


import sys,json


fp = open('D:\Coding\py3\json\json.json','w',encoding='utf-8')  #打开你要写得文件test2.txt
lines = open('D:\Coding\py3\json\json',encoding='utf-8').readlines()  #打开文件，读入每一行
for s in lines:
    fp.write( s.replace('}}','}}\n'))    # replace是替换，write是写入
fp.close()