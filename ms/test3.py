#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/4/9 0009 10:51
# software: PyCharm

'''
a_tuple=('crazyit',20,5.6,'fkit',-17)
print(a_tuple)
print(a_tuple[0])
print(a_tuple[1])
print(a_tuple[-1])
print(a_tuple[-2])
'''


'''
a_tuple = ('crazyit',20,5.6,'fkit',-17)
print(a_tuple[1: 3])
print(a_tuple[-3: -1])
print(a_tuple[1: -2])
print(a_tuple[-3: 4])

b_tuple=(1,2,3,4,5,6,7,8,9)
print(b_tuple[2: 8: 2])
print(b_tuple[2: 8: 3])
print(b_tuple[2: -2: 2])
'''

'''
a_tuple=('crazyit',20,-1.2)
b_tuple=(127,'crazyit','fkit',3.33)

sum_tuple=a_tuple + b_tuple
print(sum_tuple)
print(a_tuple)
print(b_tuple)

print(a_tuple+(-20,-30))

a_list=[20,30,50,100]
b_list=['a','b','c']

sum_list=a_list+b_list

print(sum_list)
print(a_list+['fkit'])
'''

"""
a_tuple=('crazyit',20)
mul_tuple=a_tuple * 3
print(mul_tuple)

a_list = [30,'Python',2]
mul_list = a_list * 3
print(mul_list)

# order_endings=('st','nd','rd') + ('th') * 17 + ('st','nd','rd') + ('th') * 7 + ('st,')
order_endings = ('st', 'nd', 'rd')\
    + ('th',) * 17 + ('st', 'nd', 'rd')\
    + ('th',) * 7 + ('st',)
print(order_endings)
day= input("输入日期(1-31)：")
day_int=int(day)
print(day+order_endings[day_int - 1])
"""

"""
a_tuple=('crazyit',20,-1.2)
print(20 in a_tuple)
print(1.2 in a_tuple)
print('fkit' not in a_tuple)

aa_tuple=(20,10,-2,15.2,102,50)
print(max(aa_tuple))
print(min(aa_tuple))
print(len(aa_tuple))

b_list=['crazyit','fkit','Python','Kotlin']
print(max(b_list))
print(min(b_list))
print(len(b_list))
"""

"""
序列封包和序列解包
vals= 10,20,30
print(vals)
print(type(vals))
print(vals[1])
a_tuple=tuple(range(1,10,2))
a,b,c,d,e=a_tuple
print(a,b,c,d,e)
a_list=['fkit','crazyit']
a_str,b_str=a_list
print(a_str,b_str)



x,y,z=10,20,30
print(x,y,z)

xyz=10,20,30
x,y,z=xyz

x,y,z=y,z,x     #位置发生了变化
print(x,y,z)


first,second,*rest=range(10)
print(first)
print(second)
print(rest)

*begin,last=range(10)
print(begin)
print(last)

first,*middle,last=range(10)
print(first)
print(middle)       #这里middle只会匹配0到8
print(last)
"""


""""
a_tuple=('crazyit',20,-1.2)
a_list=list(a_tuple)
print(a_list)
a_range=range(1,5)
print(a_range)
b_list=list(a_range)
print(b_list)
c_list=list(range(4,20,3))
print(c_list)


aa_list=['crazyit',20,-1.2]
aa_tuple=tuple(aa_list)
aa_range=range(1,5)
print(aa_range)
bb_tuple=tuple(aa_range)
print(bb_tuple)
cc_tuple=tuple(range(4,20,3))
print(cc_tuple)
"""

"""
a_list=['crazyit',20,-2]
a_list.append('fkit')
print(a_list)

a_tuple=(3.4,5.6)
a_list.append(a_tuple)
print(a_list)

a_list.append(['a','b'])
print(a_list)
print(a_list[4][0])


b_list=['a',30]
b_list.extend((-2, 3.1))
print(b_list)
b_list.extend(['C','R','A'])
print(b_list)
b_list.extend(range(97,100))
print(b_list)

c_list=list(range(1,6))
print(c_list)
c_list.insert(3,'CRZAY')
print(c_list)
c_list.insert(3,tuple('crazy'))
print(c_list)
"""

"""
a_list=['crazyit',20,-2.4,(3,4),'fkit']
del a_list[2]
print(a_list)
del a_list[1: 3]
print(a_list)
b_list=list(range(1,10))
del b_list[2: -2: 2]
print(b_list)
del b_list[2: 4]
print(b_list)

name='crazyit'
print(name)
del name

c_list=[20,'crazyit',30,-4,'crazyit',3.4]
c_list.remove(30)
print(c_list)
c_list.remove('crazyit')
print(c_list)
c_list.clear()
print(c_list)
"""


"""
a_list=[2,4,-3.4,'crazyit',23]
a_list[2]='fkit'
print(a_list)
a_list[-2]=9527
print(a_list)

b_list=list(range(1,5))
print(b_list)
b_list[1: 3]=['a','b']
print(b_list)


bb_list=list(range(1,5))
print(bb_list)
bb_list[1:3]=['a','b']
print(bb_list)

bb_list[2: 2]=['x','y']
print(bb_list)

bb_list[2: 5] = []
print(bb_list)

bb_list[1: 3]='Charlie'
print(bb_list)

c_list=list(range(1,10))
c_list[2: 9: 2]=['a','b','c','d']
print(c_list)
"""


"""
print(dir(list))

a_list=[2,30,'a',[5,30],30]

print(a_list.count(30))
print(a_list.count([5,30]))


a_list=[2,30,'a','b','crazyit',30]
print(a_list.index(30))
print(a_list.index(30,2))
print(a_list.index(30,2,4))
"""

"""
stack=[]
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


a_list=list(range(1,8))
a_list.reverse()
print(a_list)
"""

"""
a_list=[3,4,-2,-30,14,9.3,3.4]
a_list.sort()
print(a_list)
b_list=['Python','Swift','Ruby','Go','Kotlin','Erlang']
b_list.sort()
print(b_list)

b_list.sort(key=len)
print(b_list)
b_list.sort(key=len,reverse=True)
print(b_list)

def len_cmp(x, y):
    return 1 if len(x) > len(y) else (-1 if len(x) < len(y) else 0)
b_list.sort(len_cmp)
print(b_list)
"""

