# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 19:17
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 09 编码2.py
# @Software: PyCharm

# str1 = 'barry'
# print(str1.upper())
# bytes
# b1 = b'barry'
# print(b1.upper())

# s1 = '中国'
# b1 = s1.encode('utf-8')
# print(b1)

# 转换；
# str ---->bytes
# unicode ---> utf-8
# s1 = '中国'
# # # b1 = s1.encode('utf-8')  # 编码
# # # print(b1)
# # # # utf-8 ----> unicode
# # # s2 = b1.decode('utf-8') # 解码
# # # print(s2)

s1 = '中国'
b1 = s1.encode('gbk')  # 编码
print(b1)
# utf-8 ----> unicode
s2 = b1.decode('gbk') # 解码
print(s2)

# gbk ---> utf-8
b1 = b'\xd6\xd0\xb9\xfa'
s1 = b1.decode('gbk')  # unicode
b2 = s1.encode('utf-8')
print(b2)