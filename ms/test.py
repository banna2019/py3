#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/4 0004 20:38
# software: PyCharm


'''
print(type('a'))
print((1))

user_name='Charlie'
user_age=8
print("读者名: %s  年龄: %s" % (user_name,user_age))
print("读者名: {0}  年龄: {1}".format(user_name,user_age))
'''


'''
print(40)
print(50)
print(60)

print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")

# print(40,'\r',end="")
# print(50,'\r',end="")
# print(60,'\r',end="")
'''

'''
f=open("poem.txt","w")
print('沧海月明珠有泪',file=f)
print('蓝回日暖玉生烟',file=f)
f.close()
'''

'''
import keyword

#查看关键字
print(keyword.kwlist)

one_million = 1000000
print(one_million)
price = 234_234_234         #python2不支持在数值中使用下划线
android=12341234
'''

'''
af1=5.23455556
print(af1)

af2=25.2345
print(type(af2))

f1=5.12e2
print(f1)

f2=5e3
print(f2)
print(type(f2))
'''

'''
复数
ac1=3+0.2j
print(ac1)
print(type(ac1))

ac2=4-0.1j
print(ac2)

print(ac1+ac2)


import  cmath
ac3=cmath.sqrt(-1)
print(ac3)
'''


"""
s = '''"Let's go fishing", said Mary.
"OK, Let's go", said her brother.
they walked to a lake'''
print(s)


s2 = 'The quick brown fox \
jumps over the lazy dog'
print(s2)


num = 20 + 3 / 4 + \
    2 * 3
print(num)

#原始字符串以“r”开头,原始字符串不会把反斜线当成特殊字符.因此,上面的 Windows 路径可直接写成 r'G:\publish\codes\02\2.4'.
s1 = r'G:\publish\codes\02\2.4'
print(s1)

# 原始字符串包含的引号,同样需要转义
s2 = r'"Let\'s go", said Charlie'
print(s2)


s3 = r'Good Morning' '\\'
print(s3)

s3 = 'Good Morning' '\\'
print(s3)
"""


