#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/4 0004 22:30
# software: PyCharm

'''
字符串bytes
b1=bytes()
b2=b''
b3=b'hello'

print(b1)
print(b2)
print(b3)
print(b3[0])
print(b3[2:4])


b4 = bytes('我爱Python编程',encoding='utf-8')
print(b4)
st4=b4.decode('utf-8')
print(st4)


b5 = "学习Python很有趣".encode('utf-8')
print(b5)

st=b5.decode('utf-8')
print(st)
'''


'''
字符串转义
s = 'Hello\nCharlie\nGood\nMorning'
print(s)

s2='商品名\t\t单价\t\t数量\t\t总价'
s3='C语言小白变怪兽\t99\t\t2\t\t\t198'
print(s2)
print(s3)
'''

'''
字符串格式化
price=108
print("the book's price is %s" % price)


user="Charli"
age=8
print("%s is a %s years old boy" %(user,age))
print("{0} is a {1} years old boy".format(user,age))


num=-28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6s" % num)

num2=30
#最小宽度为0,左边补0
print("num2 is: %06d" % num2)
#最小宽度为6,左边补0,总带上符号
print("num2 is: %+06d" % num2)
#最小宽度为6,右对齐
print("num2 is: %-6d" % num2)



my_value=3.001415926535
print("my_value is: %8.3f" % my_value)
print("my_value is: %08.3f" % my_value)
print("my_value is: %+08.3f" % my_value)

the_name="Charlie"
print("the name is: %.3s" % the_name)
print("the name is: %10.2s" % the_name)
'''

'''
截取字符串
s='crazyit.org is very good'
print(s[2])
print(s[-4])

print(s[3: 5])
print(s[3: -5])
print(s[-6: -3])

print(s[5: ])
print(s[-6: ])
print(s[: 5])
print(s[: -6])

print('very' in s)
print('fkit' in s)

print(len(s))
print(len('test'))

print(max(s))
print(min(s))
'''