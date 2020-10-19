#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/5 0005 15:54
# software: PyCharm

"""
字符串大小写转换
print(dir(str))
dir(str)

a='our domain is crazyit.org'
#每个单词首字母大写
print(a.title())
#每个单词首字母小写
print(a.lower())
#每个单词首字母大写
print(a.upper())
"""


"""
去除字符串中的空格
print(dir(str))
help(str.lstrip)

s='  this is a puppy '

#删除左边的空白
print(s.lstrip())
#删除右边的空白
print(s.rstrip())
#删除两边的空白
print(s.strip())
print(s)
"""


"""
s='crazyit.org is a good site'

#是否以'crazyit'开头
print(s.startswith('crazyit'))
#是否以'site'结尾
print(s.endswith('site'))
#查找'org'出现的位置
print(s.find('org'))
#查找'org'出现的位置
print(s.index('org'))
#从索引9开始查找'org'
print(s.find('org',9))
#所有的'it'替换为'xxxx'
print(s.replace('it','xxxx'))
#替换第一个'it'为'xxxx'
print(s.replace('it','xxxx',1))
#定义替换表:97（a）->945（α）,98（b）->945（β）,116（t）->964（τ）,
table={97:945,98:946,116:964}
print(s.translate(table))
"""

'''
字符串分割、连接
table=str.maketrans('abc','αβτ')
print(table)

s='crazyit.org is a good site'

#使用空白对字符串进行分割
print(s.split())
#使用空白对字符串进行分割,分割前2个单词
print(s.split(None,2))
#使用点进行分割
print(s.split('.'))

mylist=s.split()
#使用'/'对列表mylist进行字符串连接
print('/'.join(mylist))
#使用','对列表mylist进行字符串连接
print(','.join(mylist))
'''


'''
赋值运算
d1=12.34
d2=d1+5

print("d2的值为: %g" % d2)
'''

'''
算数运算
s1='Hello,'
s2='Charlie'
print(s1+s2)

x=-5.0
x=-x
print(x)

e=5.2
f=3.1
multiply=e * f
print(multiply)

s3='crazyit'
print(s3 * 5)

#'/' 普通除法,值会有小数部位
#'//' 表示整除,值只取整数部分;丢弃小数部分
print(19/4)
print(19//4)

aa=5.2
bb=3.1
print(aa/bb)
print(aa//bb)

#取余运算
print(5 % 3 )
print(5.2 % 3.1)
print(-5.2 % -3.1)
print(5.2 % -2.9)
print(5.2 % -1.5)
print(-5.2 % 1.5)

#乘方运算
print(5 ** 2)
print(4 ** 3)
print(4 ** 0.5)
print(27 **(1/3))
'''


'''
print(5>4)
print(3**4>90)
print(20>=20.0)
print(5==5.0)
print(True==False)

print(1==True)
print(0==False)

print(True+False)
print(False-True)

import time

a =time.gmtime()
b =time.gmtime()
print(a)
print(b)
print(a==b)
print(a is b)

print(id(a))
print(id(b))

print(not False)
print(5 > 3 and 20.0 > 10)
print(4>=5 or "c" > "a")


bookName="C语言中文网Python"
price=99
version="正式版"

# if bookName.endswith('Python') and price < 50 or version == "正式版":
#     print("打算购买这套Python教程")
# else:
#     print("不购买")


if bookName.endswith('Python') and (price < 50 or version == "正式版"):
    print("打算购买这套Python教程")
else:
    print("不购买")
'''

"""
a = 5
b = 3

st= "a大于b" if a > b else "a不大于b"
print(st)

print("a大于b") if a > b else print("a不大于b")


st = print("crazyit"),'a大于b' if a > b else "a不大于b"
print(st)


st = print("crazyit"); x = 20 if a > b else "a不大于b"
print(st)
print(x)
"""

"""
c=5
d=5
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))
"""







