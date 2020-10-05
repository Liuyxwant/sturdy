# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:work liu
@file: digui
@time: 2020/7/24   9:04
@IDE:PyCharm
"""

# 3 + 2 + 1
def sum_numbers(num):
# 1.如果是1，直接返回1 -- 出⼝口
    if num == 1:
        return 1
    # 2.如果不不是1，重复执⾏行行累加:
    result = num + sum_numbers(num-1)
    # 3.返回累加结果
    return result
sum_result = sum_numbers(3)
# 输出结果为6
print(sum_result)

# lambda
# def hanshu1():
#     return 100
#
# hs = lambda : 100
# print(hs)
# print(hs())

# lambda 参数
def hanshu1(a=1,b=2,*args):
    return a+b,args
print(hanshu1())

hs = lambda *args: args
print(hs)
print(hs(5,7,2435))

hss = lambda **kwargs:kwargs
print(hss(name="ni",shuliang = 2))

print((lambda a,b:a+b) (123,1))

print((lambda a,b: a if a>b else b)(3,4))



students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}]
students.sort(key=lambda x:x["age"])
print(students)


# 绝对值 abs()
def add_num(a, b):
    return abs(a) + abs(b)
result = add_num(-1, 2)
print(result)

# map
list1=[1,2,3,4]
def pingfang(x):
      return x**2
result1 = map(lambda x:x**2,list1)
print(list(result1))

# reduce
import functools
def leiji(a,b):
    return a + b
result2 = functools.reduce(lambda a,b : a+b,list1)
print(result2)

def guolu(x):
    return x % 2 == 0
result3 = filter(lambda x : x%2==0,list1)
print(list(result3))