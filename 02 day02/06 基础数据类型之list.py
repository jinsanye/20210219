# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 15:57
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 06 基础数据类型之list.py
# @Software: PyCharm

# 索引，切片。
# l1 = [100, 'alex个人简历', True, [1,2,3]]
# print(l1[0],type(l1[0]))
# print(l1[-2])
# 顾首不顾尾
# print(l1[:3])

# 列表的常用操作方法.
# 增删改查其他操作

l1 = ['alex个人简历', 'wusir', '太白金星','日天', '女神']
# 增
# append 追加
# l1.append(666)
# print(ret)

# insert插入
# l1.insert(1,'日天')
# print(l1)
# extend 迭代着追加
# l1.extend('abc')
# l1.extend([1,2,3])
# print(l1)

# 删
# pop 按照索引删除 有返回值
# ret = l1.pop(-1)
# print(ret)

# remove  按照元素删除
# l1.remove('alex个人简历')
# print(l1)

# clear
# l1.clear()
# print(l1)

# del
# del l1[0]  # 按照索引删除
# del l1[:2] # 按照切片删除
# del l1
# print(l1)

# 改
# 按照索引改值
# l1[1] = 'sb'
# 按照切片改值
# l1[:3] = 'dfsdafsdfsdaf'
# print(l1)
# 查：可以索引切片 for循环
# for i in l1:
#     print(i)
# 其他操作方法：
# print(len(l1))  # 元素个数
# count 次数
# ret = l1.count('太白金星')
# print(ret)
# index 通过元素找索引，找不到报错
# ret = l1.index('日天1')
# print(ret)
l2 = [5, 6, 4, 0, 9, 1, 7, 8]
# l2.sort()  # 从小到大
# l2.sort(reverse=True)  # 从大到小
# l2.reverse()  # 翻转
# print(l2)







# 列表的嵌套。
# l1 = [1, 2, 'taibai', [1, 'alex个人简历', 3, ]]
# '''
# 1, 将l1中的'taibai'变成大写并放回原处。
# 2，给小列表[1,'alex个人简历',3,]追加一个元素,'老男孩教育'。
# 3，将列表中的'alex个人简历'通过字符串拼接的方式在列表中变成'alexsb'。
# '''
# # print(l1[3][1])
# # new = l1[3][1] + 'sb'
# l1[3][1] = l1[3][1] + 'sb'
# print(l1)

#  元组： 基础数据类型之一：tuple
# 存储数据，重要的数据。
# tu1 = (100, True, [1,2,3])
# 元组增删改，可以查询
# 元组也有索引切片。
# print(tu1[0])
# for i in tu1:
#     print(i)

# tu1 = (100, True, [1,2,3])
# tu1[-1].append(666)
# print(tu1)
# tuple


# range 可以视为一个可控的数字范围的列表，多于for循环结合。
# for i in range(1,10):  # [1,2,3,4,...9]
#     print(i)
# for i in range(20):  # [0,1,2,3,4,...19]
#     print(i)

# for i in range(1,10,2):  # [1,2,3,4,...9]
#     print(i)
# print(range(10))
# for i in range(10, 1, -1):
#     print(i)

# l1 = ['alex个人简历', 'wusir', '太白金星','日天', '女神']
# range 打印列表的索引
# for index in range(len(l1)):
#     print(index)