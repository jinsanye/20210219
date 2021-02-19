# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 10:33
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04 运算符.py
# @Software: PyCharm

#逻辑运算: and or not
# 优先级：() > not > and > or ,同一优先级从左至右依次计算。
# 1,运算符两边全部是比较运算
# print(1 > 2 and 3 < 4 and 2 > 7 or 4 < 5 )
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# print(False or 9 < 8)


# 2,运算符两边全部是数值
'''
x or y if x is True return x else y

'''
# print(1 or 3)
# print(2 or 3)
# print(-1 or 3)
# print(0 or 3)
# print(1 or 3 or 0 or -1)

# print(1 and 3)
# print(2 and 3)
# print(-1 and 3)
# print(0 and 3)
'''
int ---> bool: 非0即True，0即False
int ---> bool: True  1，False  0
# i = 0
# print(bool(i))
# print(int(True))
# print(int(False))

'''
# print(1 or 3 and 6 or 5 and 7 or 8)
# 3,运算符两边即是比较又是数值
# print(1 > 2 or 3 and 4)
# 成员运算： in     not in
# s1 = 'abcde'
# s2 = 'ac'
# print(s2 in s1)
#
# if s2 in s1:
#     print(333)
# else:
#     print(111)