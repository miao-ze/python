
#类方法
# class Dog(object):
#     name = 'pipi'
#     def __init__(self,name):
#         self.name = name
#     @classmethod        #把实例本身，改变为了类本身
#     def name1(self):
#         print(f'小狗的名字是：{self.name}')
#
# xiaopi = Dog('xiaopi')
# xiaopi.name1()

#静态方法
# class Stuendt(object):
#     def __init__(self,name):
#         self.name = name
#     @staticmethod
#     def eat(self):
#         print(f'{self.name}吃饭')
#
# s = Stuendt('jack')
# s.eat(s)
# s.eat()


# 3.属性方法property    '''可将方法变为属性'''
# class Stuendt(object):
#     def __init__(self,name):
#         self.name = name
#     @property
#     def fly1(self):
#         print(self.name,"在飞")
#
#
# s = Stuendt('jack')
# s.fly1


#反射 映射 自省
# getattr()   获取
# hasattr()   判断
# setattr()   赋值
# delattr()   删除
'''通过字符串的形式对对象进行操作'''
# class Stuendt(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# jack = Stuendt('jack',22)
# if hasattr(jack,'name'):
#     print('有这个属性')

# i = getattr(jack,'name')
# print(i)


#几个加下划线的方法（重要）

# 1.len（）方法
# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __len__(self):
#         print('my word')
#         return len('my word')
# p = Person('jack',22)
# len(p)















