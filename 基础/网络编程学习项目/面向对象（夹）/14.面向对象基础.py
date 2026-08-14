# 目标
'''
1.理解面向对象
2.类和对象
3.添加和获取对象属性
4.魔法方法
'''

# 类和对象的关系：用类去创建一个对象
# 类相当于制造机器的图纸，对象相当于用图纸制造后的机械（只有先设计出机械图纸，才可一制造出所需要的机械）

#需求：洗衣机，功能：能洗衣服


# # 1.定义洗衣服(定义类)
# class Washer():
#     name = 'haier'
#     def wash(self):
#         print('能洗衣服')
#
# # # 2.创建对象
# # #变量名 = 类名
# haier = Washer()
# # 3.验证成果
# # print(haier())
# #使用wash的功能---实例方法/对象方法---变量名.wash()
# haier.wash()
# print(f'my name is {haier.name}')

# 二.类中的self()
# self指的是调用该函数的对象
# class Washer():
#     def wash(self):
#         print('能洗衣服')
#         print(self)
# haier = Washer()
# # print(haier)
# haier.wash()
#由于打印对象和打印self得到的内存地址相同,所以self()指的是调用该函数的对象
'''
#1. 一个类创建多个对象   2.多个对象都调用时self的地址是否相同
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)
haier1 = Washer()
haier1.wash()
haier2 = Washer()
haier2.wash()
#不同对象的地址是不同的

# 利用一个类来创建两个对象
class Person():
    def named(self,name):
        self.name = name
    def speak(self):
        print(f'hello my name is {self.name}')

people1 = Person()
people1.named('tom')
people1.speak()


'''

# 三.添加和获取对象的属性
# 属性即是特征,如:洗衣机的高度,宽度,重量等
# 对象的属性既可以在类的外面添加和获取,也可以在类的里面添加和获取
# 1.1 类的外面添加对象的属性
# class Washer():
#     def wash(self):
#         print('洗衣服')
#
#
# haire1 = Washer()
# # # #添加属性 语法: 对象名.属性名 = 值
# haire1.width = 400
# haire1.height = 500
# # # # 1.2 类外面获取对象属性
# # # # 语法:  对象名.属性名
# print(f'洗衣机的宽度是: {haire1.width}')
# print(f'洗衣机的高度是: {haire1.height}')


# 1.3 在类的里面获取对象属性
# 语法: self.属性名
# class Washer():
#
#     def wash(self):
#         print('洗衣服')
#     def print_info(self):
#         # self.属性名
#         #类里面获取实例属性
#         print(f'洗衣机的宽度是: {self.width}')
#         print(f'洗衣机的高度是: {self.height}')
#
#
# # #
# # # #创建对象
# haire1 = Washer()
# # 添加属性
# haire1.width = 400
# haire1.height = 500
# #进行调用
# haire1.print_info()


# 四.魔法方法
# 在pytho中，__xx__()的函数叫做魔法方法。指的是具有特殊功能的函数


# 4.1(上） _init_()   作用：初始化对象

# class Washer():
#     def __init__(self):
#         #添加实例属性
#         self.width = 500
#         self.height = 300
#
#     def print_into(self):
#         print(f'洗衣机的宽度是: {self.width}')
#         print(f'洗衣机的高度是: {self.height}')
#
# haier = Washer()
# haier.print_into()

# 4.1（下） 带参数的__init__(self)
# '''一个类可以创建多个对象，对多个对象设置不同的初始化值（即设置相同属性的不同的值）'''

# class Washer():
#     def __init__(self,width,height):   #还定义的两个形参
#         #添加了两个实例属性（且其对应的值不是固定的）
#         self.width = width      #取得是width形参接收到的数据
#         self.height = height    #取得是height形参接收到的数据
#     def print_info(self):
#         print(f'次型号为{self.name}')
#         print(f'洗衣机的宽度是: {self.width}')
#         print(f'洗衣机的高度是: {self.height}')
#
# list1 = []
# for i in range(1,3):
#     mode1 = input(f"请输入第{i}种冰箱的型号：")
#     width = input('请输入次型号的宽度：')
#     height = input('请输入次型号的高度：')
#     fright = Washer(width,height)
#     fright.name = mode1
#     fright.print_info()
#
# with open('bright.txt','w+') as file1:


# haier1 = Washer(10,20)      #魔法方法不用手动去调用，其在创建对象是会自动调用
# haier1.print_info()
#
#
# haier2 = Washer(24,67)      #魔法方法不用手动去调用，其在创建对象是会自动调用
# haier2.print_info()


# 4.2 __str__()
# 如果类中定义了 __str__() ，则会打印从这个方法中return的数据 （要打印对象）

# class Washer():
#     def __init__(self,height):
#         self.height = height
#     def __str__(self):
#         print(f'高度：{self.height}')
#         return '这是本产品的数据参数'
# haier = Washer(100)
# print(haier)   #注意是打印对象


# 4.3 __del__()  当删除对象时，python解释器也会默认调用__del__()方法

# class Washer():
#     def __init__(self,height):
#         self.height = height
#     def __del__(self):
#         print('对象已被删除')
#
# haier = Washer(12)








