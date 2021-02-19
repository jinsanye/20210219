# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 10:12
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 03 格式化输出.py
# @Software: PyCharm

# 格式化输出
#
# name = input('请输入姓名')
# age = input('请输入年龄')
# hobby = input('请输入爱好')
# job = input('请输入你的工作')
# # msg = '我的姓名' + name + '我的年龄' + age。。。。。。。
#
# # msg = """------------ info of Alex Li -----------
# # Name  : Alex Li
# # Age   : 22
# # job   : Teacher
# # Hobbie: woman
# # ------------- end -----------------"""
# # why：你要制作一个字符串类的模板，让其一些位置上元素变成动态可输入，用字符串拼接只能做简单的，对于复杂的
# # 格式化输出。
# # % 占位符 s 字符串 d/i 数字 f 浮点型 r
# msg = """------------ info of %s -----------
# Name  : %s
# Age   : %s
# job   : %s
# Hobbie: %s
# ------------- end -----------------""" % (name,name,age,job,hobby)
# print(msg)


# 坑
# 只是想在格式化输出中单纯的表示% 不想让%当成%    解决：%%
# msg = '我叫%s,今年%s岁,学习进度3%%' % ('宁哥', 28)
# print(msg)
