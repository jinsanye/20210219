# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 17:31
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 07 基础数据类型之dict.py
# @Software: PyCharm

dic = {'name': 'alex个人简历', 'age': 46, 'sex': 'laddyboy'}

# 增删改查其他方法
# 增：
# 有则修改，无责增加
# dic['high'] = 175
# print(dic)
# dic['name'] = '日天'
# print(dic)

# 有责不变，无责增加
# dic.setdefault('weight',200)
# print(dic)
# dic.setdefault('age',73)
# print(dic)

# 删除

# pop 按照key删除键值对,有返回值
# ret = dic.pop('name')
# print(ret)
# clear
# dic.clear()
# print(dic)

#
# del dic
# del dic['name']

# 改
# dic['name'] = '日天'

# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex个人简历","weight":75}
# dic2.update(dic)   # 将dic的键值对覆盖添加到dic2中，dic不变。
# print(dic2)
# print(dic)

# 查
# print(dic['name'])
# print(dic['name1'])
# ret = dic.get('name')
# ret = dic.get('name1', '没有此键')
# print(ret)

#
# for i in dic:
#     print(i,dic[i])
# 其他方法：

# dic.keys() dic.values() dic.items()
# print(dic.keys(),type(dic.keys()))

# for key in dic.keys():
#     print(key,type(key))

# for v in dic.values():
#     print(v)

# 分别赋值
# a, b = 1, 4
# print(a,b)
# a, b = (1,4)
# a, b = [[1,2,3],'alex个人简历']
# print(a,b)
# print(dic.items())  # dict_items([('name', 'alex个人简历'), ('age', 46), ('sex', 'laddyboy')])
# for k,v in dic.items():
#     print(k,v)
# print(list(dic.items()))

# 嵌套
# dic = {
#     'name_list': ['张三', '李四', 'BARRY'],
#     1:{'name':'taibai', 'age': 18}
#     'barry': {}
# }
# 1，给列表追加一个值：'王五'
# dic['name_list'].append('王五')
# print(dic)
# 2，将BARRY 变成全部小写
# print(dic['name_list'][-1].lower())
# dic['name_list'][-1] = dic['name_list'][-1].lower()
# print(dic)
# 3，给{'name':'taibai', 'age': 18} 增加一个键值对 sex: 男。
# print(dic[1])
# dic[1]['sex'] = '男'
# print(dic)