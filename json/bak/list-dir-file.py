#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/13 0013 15:25
# software: PyCharm

import os,sys

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('{0}{1}'.format(filepath,allDir))
        if os.path.splitext(child)[1] == ".txt":
            print(child.encode('utf-8'))


if __name__ == '__main__':
    eachFile(r'D:\Coding\py3\json')