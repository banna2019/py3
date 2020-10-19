#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/12 0012 23:27
# software: PyCharm

import os
import sys,json

def all_path(dirname):
    for maindir,subdir,file_name_list in os.walk(dirname):
        #print("1:",maindir) #当前主目录
        #print("2:",subdir) #当前主目录下的所有目录
        #print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir,filename)#合并成一个完整路径
            if os.path.splitext(apath)[1] == ".txt":
                jfile=apath
                jfile_name = os.path.splitext(apath)[0]
                # print(jfile_name)
                fp = open(jfile_name+'.json','w',encoding='utf-8')
                lines = open(jfile,'r',encoding='utf-8').readlines()
                try:
                    for s in lines:
                        fp.write(s.replace('}}','}}\n'))
                        # print(s)
                except Exception as e:
                    print(e)
                    fp.close()

if __name__ == '__main__':
    print(all_path(r'D:\Coding\py3\json'))
