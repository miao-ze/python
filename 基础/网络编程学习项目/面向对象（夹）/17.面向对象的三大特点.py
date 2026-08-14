'''
分别是：封装  继承  多态
'''

# 一。多态（多用与继承书写）
# 1.定义父类并提供公共的方法
# class Dog(object):
#     def work(self):
#         print("指哪打哪")

#2.定义子类并重写父类的公共方法
# class AmryDog(Dog):
#     def work(self):
#         print('追击敌人，，，')       #子类重写父类的方法
#
# class DrugDog(Dog):
#     def work(self):
#         print('追查毒品，，，')       #子类重写父类的方法
#
# class Penson(object):
#     def wor(self,dog):             #传入不同的对象，执行不同的代码，即不同的work函数
#         dog.work()
#
#
# adog = AmryDog()
# ddog = DrugDog()
#
# 3.传入不同的对象（实现不同的效果）
# wo = Penson()
# wo.wor(ddog)
# wo.wor(adog)


# 二。类属性
'''
类变量和实例变量
'''
# class Dog():
#     tooth = 10
#
# wangchai = Dog()
# xiaohei = Dog()
#
# print(Dog.tooth)       #通过类来访问
# print(wangchai.tooth)  #通过对象来访问
# print(xiaohei.tooth)

#  修改类属性
# class Dog():
#     tooth = 10
#
# wangchai = Dog()
# xiaohei = Dog()
#
#
# #1.通过类修改
# Dog.tooth = 20
# #2.通过对象来修改
# wangchai.tooth = 15
#
#
# print(Dog.tooth)       #通过类来访问
# print(wangchai.tooth)  #通过对象来访问
# print(xiaohei.tooth)

#类方法
#1.第一类：私有类属性。用类方法获取这个私有类属性
class Dog():
    id = 9332
    def __init__(self):
        self.__name = "xiaolan"
    def jieko(self):

        return (self.__name)



dog = Dog()
print(dog.jieko())
#     #定义类方法
#     @classmethod         #装饰器
#     def get_tooth(cls):
#         return cls.__tooth
#
# #2,创建对象，调用类方法
# wanghcai = Dog()
# result = wanghcai.get_tooth()
# print(result)    #访问成功

# 2.静态方法
''''''
# 1.定义类：定义静态方法
# class Dog():
#     @staticmethod
#     def print():
#         print('这是一个静态方法')
#
# #2.创建对象
# xiaohei1 = Dog()
# xiaohei1.print()   #用对象访问
# Dog.print()        #用类访问






