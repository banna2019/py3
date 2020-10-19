#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/7/17 0017 14:21
# software: PyCharm

import os
import sys,json
import os



def source_js():
    # for files in jsfile:
        for line in open('D:\Coding\py3\json\\ta.txt','r',encoding='utf-8'):
            # print(line)
            json_dicts=json.loads(line)
            print(json_dicts)
            # if isinstance(json_dicts,dict):
            #     for key,vva in json_dicts.items():
            #         if key=='type':
            #             print('key1--:  {0}    value1--:  {1}'.format(key,vva))
            #         elif key=='database':
            #             print('key1--:  {0}    value1--:  {1}'.format(key,vva))
            #         elif key=='table':
            #             print('key2--:  {0}    value2--:  {1}'.format(key,vva))
            #         elif key=='type':
            #             print('key3--:  {0}    value3--:  {1}'.format(key,vva))
            #         elif key=='ts':
            #             print('key4--:  {0}    value4--:  {1}'.format(key,vva))
            #         elif key=='xid':
            #             print('key5--:  {0}    value5--:  {1}'.format(key,vva))
            #         elif key=='commit':
            #             print('key6--:  {0}    value6--:  {1}'.format(key,vva))
            #         elif key=='xoffset':
            #             print('key7--:  {0}    value7--:  {1}'.format(key,vva))
            #         elif key=='data':
            #             # print(vva)
            #             jsdata=vva
            #             if isinstance(jsdata,dict):
            #                 for key8,vva8 in jsdata.items():
            #                     print('key8--:  {0}    value8--:  {1}'.format(key8,vva8))
            #         elif key=='old':
            #             # print(vva)
            #             jsold=vva
            #             if isinstance(jsold,dict):
            #                 for key9,vva9 in jsold.items():
            #                     print('key9--:  {0}    value9--:  {1}'.format(key9,vva9))


if __name__ == '__main__':
    # print(all_path('D:\Coding\py3\json'))
    # all_rep('D:\Coding\py3\json')
    source_js()
