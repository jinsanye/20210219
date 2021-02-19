# -*- encoding: utf-8 -*-
'''
此py文件的：......
'''
# print('hello 世界')
"""
# 变量：
print(1+2+3+4+5)
print((1+2+3+4+5)*5/2)
print(((1+2+3+4+5)*5/2 + 100)/5)
print(((((1+2+3+4+5)*5/2 + 100)/5+3))/6 + 78)

x = 1+2+3+4+5
y = x*5/2
z = (y+100) /5
w = (z + 3) /6 + 78

msg = '今天python周末班2期开班了....gfdjggkfdlgjdklgjsdfkl'

m1 = '今天python周末班2期开班了....gfdjggkfdlgjdklgjsdfkl' + '6:30'
m1 = msg + '6:30'

4e = 'alex个人简历'  # False
q_ = 111  # True
__ = 67  # False
_ = 567  # True
3# = 45  # False
_3 = 66  # True
tr8_= 33 # True


age1 = 12
age2 = age1
age3 = age2
age2 = 36
print(age1,age2,age3)  
# 12 36 12  12 12 12 12 36 36 

age1 = 12
age1 = 13
print(age1)
age1 = 14
"""

# 常量：
'''
BIRTH_OF_CHINA = 1949
BIRTH_OF_CHINA = 1980
print(BIRTH_OF_CHINA)
'''

# 基础数据类型：
#i1 = 100
#i2 = 20
#print(i1 + i2)

s1 = "太白金星"
s2 = '太白金星'
s3 = 'I\'m taibai, my age is 18'
s3 = "I'm taibai, my age is 18"
#print(s3)
# ''' ''' """ """ 换行的字符串需要三引号
msg = '''
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
'''
#print(msg)
# 
# 字符串 可以相加，可以与数字相乘
s1 = 'alex个人简历'
s2 = 'sb'
s3 = s1 + s2
#print(s3)
# 
#s4 = '坚强'
#print(s4 * 8)
#print(1 > 2)
#print(3 > 2)
#s5 = 'True'
#b1 = True
#print(s5, b1)
#print(s5, type(s5))
#print(b1, type(b1))

# 用户交互input
# input出来的数据全部都是str类型。
'''
name = input('请输入姓名：')
age = input('请输入年龄：')
print(name, age)
print(type(name))
# '我的姓名xx,我的年龄xx,我的性别xx.'

#name = input('请输入姓名：')
#age = input('请输入年龄：')
#sex = input('请输入性别：')
#msg = '我的姓名是' + name + ',我的年龄是' + age + ',我的性别是' + sex
#print(msg)
#print('我的名字', '是', '太白')
#print('我的姓名是' + name + ',我的年龄是' + age + ',我的性别是' + sex)
'''
# if
# 补充 
#str ---> int  前提： 全部由数字组成的字符串才能转化成int
s1 = '100a'
#i1 = int(s1)
#print(i1,type(i1))
#int ---> str  
i1 = 1000
#print(type(str(i1)))

# 单独if
'''
age = int(input('请输入年龄'))

if age > 18:
    print('做你想做的事儿')
print(666)	
'''

# if else
'''	
age = int(input('请输入年龄'))

if age > 18:
    print('做你想做的事儿')
else:
    print('安心上学....')
'''

	
# if elif elif ...
"""
num = input('请输入数字：')

if num == '5':
    print('请你吃饭')
elif num == '1':
    print('带你去香港')
elif num == '3':
    print('请你去大宝剑')
"""

# if elif elif ... else 
'''
score = int(input("输入分数:"))

if score > 100:
    print("我擦，最高分才100...")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")
print(666)
'''
# if 嵌套
'''
code = 'ABCD'
your_code = input('输入验证码')
username = input('请输入用户名')
password = input('请输入密码')
if your_code == code:
    if username == 'alex个人简历' and password == '123':
	    print('登录成功')
    else:
	    print('用户名或者密码错误')
else:
    print('您输入的验证码错误')
'''

# while 循环
'''
while True:
    print('光年之外')
    print('千里之外')
    print('美人鱼')
    print('沙漠骆驼')

flag = True
	
while flag:
    print('光年之外')
    print('千里之外')
    print('美人鱼')
    print('沙漠骆驼')
    flag = False

flag = True
while flag:
    print('光年之外')
    print('千里之外')
    print('美人鱼')
    flag = False
    print('沙漠骆驼')
    

count = 1
flag = True
while flag:
    print(count)
    count = count + 1
    if count == 101:
	    flag = False

count = 1
while count < 101:
    print(count)
    count = count + 1
'''

# break continue
# break: 遇到break直接结束循环。
'''
while True:
    print(111)
    print(222)
    break
    print(333)
print(555)
'''

# continue
'''
while True:
    print(111)
    print(222)
    continue
    print(333)
'''

# 1 2 3 4 5 6 8 9 10
'''
count = 0
while count < 10:
    count = count + 1
    if count == 7:
	    continue
    print(count)
''' 

#while else: while 循环中只要被break打断，则不执行else语句。
count = 0
while count <= 5 :
    count += 1
    if count == 3:
	    break
    print(count)

else:
    print("循环正常执行完啦")

	
	
	
	
	
	






