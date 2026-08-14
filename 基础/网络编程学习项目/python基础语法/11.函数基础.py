# 快速体验
# 需求：重复ATM取钱功能

# def a():
#     print('显示余额')
#     print('存款')
#     print('取款')
#                         #先定义在调用
# print('密码正确登入成功.')
# #显示功能界面
# a()
#
# print('查询余额完毕.')
# a()
# #显示功能界面
# print('取了2000元钱.')
# #显示功能界面
# a()
#
# def b():
#     print('hello world')
# # b()

# 一。函数的参数的作用
# 计算两个数的加法
# 1.先不用参数进行
# def jia():
#     result = 1 + 4
#     print(result)
# jia()
# 2,用参数进行          (自定义数字加法运算）
# def jia1(a,b):    #（这里的a，b。叫做形参）
#     result = a + b
#     print(result)
# a = int(input('请输入数字1：'))
# b = int(input('请输入数字2：'))
# jia1(2.4)           #（这里的a，b。叫做实参）

# 二。函数的返回值
# 简单的例子
# def buy():
#     x = '枪'
#     print(x)
#     return x
# buy()
# good = buy()
# print(good)

# def buy():
#     return '烟'
#     print('ok')
#
# goods = buy()
# print(goods)


# 应用案例
# 需求：制作一个计算器
# def jijuan(a,b):
#     return a + b
# a = int(input('请输入将要计算的数字1：'))
# b = int(input('请输入将要计算的数字2：'))
# result = jijuan(a,b)
# print(f'{a} + {b} =',result)

# 判断时间吃早饭
# time = int(input('请输入现在的时间：'))
# def work():
#     if 6 <= time <= 10:
#         print('eat breakfast')
#     elif 10 < time <= 14:
#         print('eat lunch')
#     else:
#         print('eat dinner')
#  work()
#
# def time():
#     if 6 <= times <= 10:
#         return f'现在是{times}点，吃早饭'
#     elif 10 < times <= 14:
#         return f'现在是{times}点，吃午饭'
#     else:
#           return f'现在是{times}点，吃晚饭'
# times = int(input('请输入现在的时间：'))
# a = time()
# print(a)

# def subject(math,chinese,english):
#     maxs = max(math,chinese,english)
#     mins = min(math,chinese,english)
#     zong = (math) + (chinese) + (english)
#     return maxs,mins,zong
# math = int((input('输入您的数学成绩：')))
# chinese = int((input('输入您的语文成绩：')))
# english = int((input('输入您的英语成绩：')))
# a = subject(math,chinese,english)
# print(f'此次小红的最高分是：{a[0]} \n此次小红的最低分是：{a[1]} \n此次小红的总成绩是：{a[2]}')

# 二。函数的说明文档
# 函数：help（）
# def sum_mul(a ,b):
#     '''求和函数'''
#     return a + b
# help(sum_mul)

# 三。函数的嵌套
# 例子        在A中套用B
# 方式一.
# def a():
#     print(11111)
#     print(22222)
#     print(33333)
# def b():
#     a()
#     print(44444)
#     print(55555)
#     print(66666)
# b()
# 方式二.
# def a ():
#     print(1111)
#     def b():
#         print(2222)
#     b()
# a()

# 嵌套应用值打印图像
# 1.方法一
# i = 0
# while i < 5:
#     def xian():
#         a = '--'
#         print(a * 20)
#         return '五条线条横线'
#     xian()
#     i += 1
# b = xian()
# print(b)

# 2.方法二
# def xian():
#     a = '--'
#     print(a * 20)
#
# def lins(mul):
#     i = 0
#     while i < mul:
#         xian()
#         i += 1
# lins(5)

# 函数计算
# 1.求和
# def he(a,b,c):
#     return a + b + c
# i = he(1,2,3)
# print(i)
# 2.求平均值
# def he(a,b,c):
#     return (a + b + c) / 3
# i = he(1,2,3)
# print(i)