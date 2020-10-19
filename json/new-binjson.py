#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/16 0016 20:23
# software: PyCharm


import os
import sys,json
import os


def all_rep(dirname):
    for maindir,subdir,file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir,filename)
            if os.path.splitext(apath)[1] == ".txt":
                jfile=apath
                jfile_name = os.path.splitext(apath)[0]
                # print(jfile_name)
                fp = open(jfile_name+'.json','w',encoding='utf-8')
                lines = open(jfile,'r',encoding='utf-8').readlines()
                try:
                    for s in lines:
                        fp.write(s.replace('}}','}}\n'))
                except Exception as e:
                    print(e)
                    fp.close()

def all_path(dirname):
    result = []

    for maindir,subdir,file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir,filename)
            if os.path.splitext(apath)[1] == ".json":
                result.append(apath)

    return result

def source_js(jsfile):
    for files in jsfile:
        for line in open(files,'r',encoding='utf-8'):
            json_dicts=json.loads(line)
            # print(json_dicts)
            if isinstance(json_dicts,dict):
                for key,vva in json_dicts.items():
                    if vva=='insert':
                        print('key1--:  {0}    value1--:  {1}'.format(key, vva))
                    elif vva=='update':
                        print('key2--:  {0}    value2--:  {1}'.format(key,vva))
                    elif vva=='delete':
                        print('key3--:  {0}    value3--:  {1}'.format(key,vva))
                    elif str(vva)=='table-alter':
                        print('key4--:  {0}    value4--:  {1}'.format(key,vva))
                    elif vva=='drop':
                        print('key5--:  {0}    value5--:  {1}'.format(key,vva))


                    # elif key=='xoffset':
                    #     print('key6--:  {0}    value6--:  {1}'.format(key,vva))
                    # elif key=='data':
                    #     # print(vva)
                    #     jsdata=vva
                    #     if isinstance(jsdata,dict):
                    #         for key7,vva7 in jsdata.items():
                    #             print('key7--:  {0}    value7--:  {1}'.format(key7,vva7))
                    # elif key=='old':
                    #     # print(vva)
                    #     jsold=vva
                    #     if isinstance(jsold,dict):
                    #         for key8,vva8 in jsold.items():
                    #             print('key8--:  {0}    value8--:  {1}'.format(key8,vva8))
                    # print(key,vva)
                    # print('key--:  {0}    value--:  {1}'.format(key,vva))

if __name__ == '__main__':
    # print(all_path('D:\Coding\py3\json'))
    # all_rep('D:\Coding\py3\json')
    source_js(all_path('D:\Coding\py3\json'))
