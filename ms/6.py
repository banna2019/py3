#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/17 0017 11:18
# software: PyCharm

"""
a_tuple=('crazyit','fkit','Charlie')
for ele in a_tuple:
        print("当前的元素是:",ele)


src_list=[12,45,3.4,13,'a',4,56,'crazyit',109.5]
my_sum=0
my_count=0
for ele in src_list:
    if isinstance(ele,int) or isinstance(ele,float):
        print(ele)
        my_sum += ele
        my_count += 1
print('总和:',my_sum)
print('平均数:',my_sum/my_count)


a_list=[330,1.4,50,'fkit',-3.5]
for i in range(0,len(a_list)):
    print("第%d个元素是 %s" % (i,a_list[i]))

my_dict={'语文':89,'数学':92,'英语':80}
for key,value in my_dict.items():
    print('key:',key)
    print('value:',value)
print('-----------------')

for key in my_dict.keys():
    print('key:',key)
    print('value:',my_dict[key])
print('------------------')

for value in my_dict.values():
    print('value:',value)

src1_list=[12,45,3.4,12,'fkit',45,3.4,'fkit',45,3.4,'fkit',45,3.4]
statistics={}
for ele in src1_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1
for ele,count in statistics.items():
    print("%s出现的次数为: %d" % (ele,count))
"""

# count_i = 0
# while count_i < 5:
#     print('count_i小于5:',count_i)
#     count_i += 1
# else:
#     print('count_i大于或等于5:',count_i)


count_i = 0
while count_i < 5:
    print('count_i小于5:',count_i)
    count_i += 1
print('count_i大于或等于5:',count_i)

a_list=[330,1.4,50,'fkit',-3.5]
for ele in a_list:
    print('元素:',ele)
else:
    print('else块',ele)