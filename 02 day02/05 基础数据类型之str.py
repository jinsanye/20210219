# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 12:05
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 05 基础数据类型之str.py
# @Software: PyCharm

# s1 = 'afds'
# s1 = ''
# print(bool(s1))

# 索引 切片（步长）
s1 = 'python周末2期'
# s2 = s1[0]
# print(s2,type(s2))
# s3 = s1[2]
# print(s3)
# print(s1[-1])
# 切片：顾首不顾尾
# s4 = s1[0:6]
# # s4 = s1[:6]
# s5 = s1[2:6]
# s6 = s1[:]
# print(s6)
# 切片+步长 [起始索引: 结尾索引: 步长]
# s7 = s1[:5:2]
# print(s7)

# 反着取值（反向步长）
# print(s1[-1:-4:-1])

# 常用操作方法
# 对字符串进行的任何操作都会形成一个新字符串，与原字符串无关。
s1 = 'aLEx'
# upper 全大写
# lower 全大写
# s2 = s1.lower()
# print(s2)
# 例子
# username = input('请输入用户名')
# password = input('请输入密码')
# code = 'afREd'.upper()
# your_code = input('请输入验证码：').upper()
# if code == your_code:
#     if username == 'barry' and password == '123':
#         print('登录成功')
# else:
#     print('验证码错误')

# strip
# 默认(指定)去除字符串两边的换行符，制表符，空格。
# lstrip  rstrip
# s1 = ' \talex\n'
# s1 = 'eareelexqw'
# s1 = '   alex个人简历   '
# s3 = s1.strip()
# s3 = s1.strip('qwer')
# print(s3)
# print(s3)
# print(s1)
# 应用：
# username = input('请输入用户名').strip()
# password = input('请输入密码').strip()
# if username == 'barry' and password == '123':
#     print('登录成功')

# s1 = '周末2期python期'
# find  通过元素找索引，找到用第一个则返回，找不到返回-1
# index 通过元素找索引，找到用第一个则返回，找不到则报错
# i = s1.find('w')
# i = s1.find('期',4,)
# i = s1.index('w')
# print(i)

s1 = '太白barry'
# startswith 判断以...为开始
# endswith 判断以...为结尾
# print(s1.startswith("太"))
# print(s1.startswith("b",2,5))
# print(s1.startswith("ba",2,5))

# s1 = 'alex个人简历 wusir 太白 日天'
# s11 = ':alex个人简历:wusir:太白:日天'
# s12 = 'alex个人简历:wusir:太白:日天'
# split 默认(可指定分隔符)以空格为分割，返回一个列表。
# 指定分隔次数
# str ----> list
# l1 = s1.split()
# print(l1)
# l2 = s11.split(':')
# l3 = s12.split(':', 1)
# print(l3)
# print(l2)

# join
# s1 = 'alex个人简历'
# l1 = ['alex个人简历', 'wusir', '太白', '日天']
# s2 = '_'.join(s1)
# s2 = '*'.join(s1)
# 前提条件：此列表必须全部是有字符串元素组成
# s2 = ' '.join(l1)
# print(s2)

s1 = 'python深圳分校 深圳是一个很美丽的城市，我爱深圳'
# replace  默认全部替换 也可以设置替换次数
# s2 = s1.replace('深圳', '北京')
# s2 = s1.replace('深圳', '北京', 1)
# print(s2)


# format
# # 第一种
# msg = '我叫{} 今年{} 性别{}'.format('太白', '18', '男')
# print(msg)
# # 第二种
# msg = '我叫{0} 今年{1} 性别{2}，我依然叫{0}'.format('太白', '18', '男')
# print(msg)
# # 第三种
# msg = '我叫{name} 今年{age} 性别{sex}'.format(name='太白', sex='男',age='18',)
# print(msg)
# s1 = 'barryafdfdafdaaa'
# # count  计算某个元素出现的次数
# i = s1.count('a')
# print(i)

# is 系列
name = 'taibai123'
# print(name.isalnum()) #字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成
# print(name.isdigit()) #字符串只由数字组成


# len 内置函数
# s1 = 'fjdsklfsjafldsfjskladfjsladfjldksa'
# print(len(s1))


# for 循环
# s1 = 'python2期'
# # while
# # print(s1[0])
# # print(s1[1])
# # print(s1[2])
#
# count = 0
# while count < len(s1):
#     print(s1[count])
#     count += 1

# for 变量 in iterable:
#     pass
# for i in s1:
#     print(i,type(i))
# for i in s1:
#     print(i + 'sb')

