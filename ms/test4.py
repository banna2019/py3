#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/16 0016 11:04
# software: PyCharm


"""
scores={'语文':89,'数学':92,'英语':93}
print(scores)
empty_dict={}
print(empty_dict)
dict2={(20,30):'good',30:'bad'}
print(dict2)


vegetables=[('celery',1.58),('brocoli',1.29),('lettuce',2.19)]
dict3=dict(vegetables)
print(dict3)
cars=[['BMW',8.5],['BENS',8.3],['AUDI',7.9]]
dict4=dict(cars)
print(dict4)


dict5=dict()
print(dict5)

dict6=dict(spinach=1.39,cabbage=2.59)
print(dict6)
"""

"""
scores={'语文': 89}
print(scores['语文'])


scores['数学']=93
scores[92]=5.7
print(scores)

del scores['语文']
del scores['数学']
print(scores)
"""

"""
cars={'BMW':8.5,'BENS':8.3,'AUDI':7.9}
cars['BENS']=4.3
cars['AUDI']=3.8
print(cars)


print('AUDI' in cars)
print('PORSCHE' in cars)
print('LAMBORGHINI' not in cars)

print(dir(dict))
"""


# cars={'BMW':8.5,'BENS':8.3,'AUDI':7.9}
# # print(cars)
# # cars.clear()
# # print(cars)
# #
# # print(cars.get('BMW'))
# # print(cars.get('PORSCHE'))
# # print(cars['PORSCHE'])
#
# cars.update({'BMW':4.5,'PORSCHE':9.3})
# print(cars)

"""
cars={'BMW':8.5,'BENS':8.3,'AUDI':7.9}
ims=cars.items()
print(type(ims))
print(list(ims))
print(list(ims)[1])
kys=cars.keys()
print(type(kys))
print(list(kys))
print(list(kys)[1])

vals=cars.values()
print(type(vals))
print(list(vals)[1])
"""

# cars={'BMW':8.5,'BENS':8.3,'AUDI':7.9}
# # print(cars.pop('AUDI'))
# # print(cars)
#
# print(cars)
# print(cars.popitem())
# print(cars)


# cars={'BMW':8.5,'BENS':8.3,'AUDI':7.9}
# k,v=cars.popitem()
# print(k,v)


# cars={'BMW':8.5,'BENS':8.3,'AUDI':7.9}
# print(cars.setdefault('PORSCHE',9.2))
# print(cars)
# print(cars.setdefault('BMW',3.4))
# print(cars)


# a_dict=dict.fromkeys(['a','b'])
# print(a_dict)
# b_dict=dict.fromkeys((13,17))
# print(b_dict)
# c_dict=dict.fromkeys((13,17),'good')
# print(c_dict)

# temp='教程是:%(name)s,价格是:%(price)010.2f,出版社是:%(publish)s'
# book={'name':'Python基础教程','price':99,'publish':'C语言中文网'}
# print(temp % book)
# book={'name':'C语言小白变怪兽','price':159,'publish':'C语言中文网'}
# print(temp % book)