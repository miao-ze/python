
# # 关于使用协程来重置生成器序列
#
# def product():
#     print('正在接受任务中......')
#     while True:
#         data = yield
#         print(f'任务数量为：{data}')
#
#
# def xiao():
#     c = product()
#     c.__next__()
#     for i in range(3):
#         print(f'发送任务中.......，任务：{i}')
#         c.send(f'任务:{i}')    # 作用是将格式的数据传递给yield的返回值
#
# xiao()


# def zz(fun):
#     def wrapper(*args,**bian):
#         print('比赛开始。。。。')
#         fun(*args,**bian)
#         print('比赛结束。。。。')
#     return wrapper
#
# @zz # first = zz(first)
# def first():
#     n = []
#     for i in range(5):
#         n.append(i)
#     print(n)
# first()


# def zz(fun):
#     class InnerClass:
#         def __init__(self,z=0):
#             self.z = z
#             self.fun = fun()
#
#         def position(self):
#             self.fun.position1()
#             print('z轴的坐标是:',self.z)
#
#     return InnerClass
#
#
# @ zz
# class OtherClass:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def position1(self):
#         print('x轴的坐标是:',self.x)
#         print('y轴的坐标是:', self.y)
#
# position = OtherClass()
# position.position()

# import py_compile
# import os
#
# # 获取当前脚本所在目录并切换过去
# os.chdir(os.path.dirname(__file__))
# # 现在工作目录是 rewrite，就可以直接使用相对路径了
# py_compile.compile('first.py', 'first.pyc')







# a = 4.2
# b = 2.1
# print(a + b)
from decimal import Decimal
# aa = Decimal('4.2')
# bb = Decimal('2.1')
# print(aa + bb)
#
# print(Decimal("6.3"))


# a = complex(2,4)
# print(a)
# b = 3 - 5j
# print(b)
# print(a +b)
# print(a * b)
# print(abs(a))

# from fractions import Fraction
#
# a = Fraction('1.1')
#
# print(type(a))

import time

def time_sleep():
    time.sleep(2.5)
    
to = time.time()
time_sleep()
print(time.time() - to)



