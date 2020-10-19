#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/12 0012 22:46
# software: PyCharm

import os

def all_path(dirname):
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir,filename)
            if os.path.splitext(apath)[1] == ".json":
                print(apath)

    # return result

if __name__ == '__main__':
    all_path('D:\Coding\py3\json')