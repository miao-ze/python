"""python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法"""
#在python中，所有类默认继承object类，object类是顶类或基类，其他类叫做生类

#父类
# class Jicheng(object):
#     def __init__(self,money_name,mul):
#         self.money_name = money_name
#         self.mul = mul
#     def print_mess(self):
#         print(f'符号：{self.money_name}，金额：{self.mul}')
#
# #子类
# class Tom(Jicheng):
#     pass
# tom = Tom('人民币',10000000000)
# tom.print_mess()

#（一）单继承
# 情景：师傅传授徒弟知识

#师傅类(属性和方法）
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子配方]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
# #徒弟类
# class A(Master):
#     pass
#
# xiaolan = A()
# print(xiaolan.kongfu)
# xiaolan.make()


# （二）多继承
# 情景：徒弟继承了一个还不够，用去学校学习新的方法
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子配方]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[通用煎饼方法]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
# class A(Master,School):
#     pass
#
# tom = A()
# print(tom.kongfu)
# tom.make()

#如果一个类继承多个父类，优先继承第一个同名属性和方法


# 四。子类重写父类同名方法和属性
# 情节：经过师傅和培训的技术后，自己潜心研制出自己的独门方法。
#
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子配方]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[通用煎饼方法]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
# class Prentice(Master,School):
#     def __init__(self):
#         self.kongfu = '[独创煎饼方法]'
#     def make(self):
#         print(f'运用{self.kongfu}来煎饼')
# wo = Prentice()
#
# print(wo.kongfu)
#
# wo.make()

# """如果子类和父类有相名的属性和方法，子类创建对象调用属性和方法的时候，调用的是子类的属性和方法"""
#
# # 拓展：-mro顺序     (调查当前这个类继承的父类有那些，及其父类的承集关系）
# print(Prentice.__mro__)


# 五。子类调用父类的同名方法和属性
# 情节：很多的顾客希望也能吃到师傅和学校制法的煎饼

'''方案一'''
# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f'大家好，我的名字是{self.name}，今年{self.age}岁了。')
#     def ds(self):
#         print('fack you')
#
# class Tom(Student):
#     def __init__(self,name,age,sex):
#         super().__init__(name,age)              #运用一：super（）方法来调用父类的方法
#         # Student.__init__(self,name,age)       #运用二：父类名().方法名（self【注意要写参数】，）
#         self.sex = sex
#     def speak(self):
#         print(f'大家好，我的名字是{self.name}，性别是{self.sex}，今年{self.age}岁了。')
#     def i(self):
#         pass
#         super().ds()
#
# tom = Tom('tom',10,'男')
# tom.i()


'''方案二'''
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子配方]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
#
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[黑马煎饼方法]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
#
# class Tom(Master,School):
#     def __init__(self):
#         self.kongfu = '[独创煎饼方法]'
#     def make(self):
#         self.__init__()         # 加自己的初始化的原因：如果不加这kongfu属性值是上一次init内kongfu属性的值
#         print(f'运用{self.kongfu},制作煎饼果子')
#         #子类调用父类的同名方法和属性：把父亲的同名属性和方法再次封装
#     def make_for_master(self):
#         #父类名.函数（）
#         Master.__init__(self)   #要在次调用初始化：因为想要调用的父类的属性和方法，而属性在init的初始化位置中，所以要再次的调用
#         Master.make(self)       #注意不要忘记位置参数
#     def make_for_school(self):
#         School.__init__(self)
#         School.make(self)
#
# tom = Tom()
# tom.make()
# tom.make_for_master()
# tom.make_for_school()
# tom.make()


# 六。多层继承
# 背景：我老了，想要把所有的技术继承给自己的徒弟

# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子配方]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
#
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[黑马煎饼方法]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
#
#
#
# class Tom(Master,School):
#     def __init__(self):
#         self.kongfu = '[独创煎饼方法]'
#     def make(self):
#         self.__init__()         # 加自己的初始化的原因：如果不加这kongfu属性值是上一次init内kongfu属性的值
#         print(f'运用{self.kongfu},制作煎饼果子')
#         #子类调用父类的同名方法和属性：把父亲的同名属性和方法再次封装
#     def make_for_master(self):
#         #父类名.函数（）
#         Master.__init__(self)   #要在次调用初始化：因为想要调用的父类的属性和方法，而属性在init的初始化位置中，所以要再次的调用
#         Master.make(self)       #注意不要忘记位置参数
#     def make_for_school(self):
#         School.__init__(self)
#         School.make(self)
#
# # 1.创建tusun类，用这个类创建对象，2用这个对象调用父类的属性和方法
# class Tusun(Tom):
#     pass
# xiaoqu = Tusun()
# xiaoqu.make()
# xiaoqu.make_for_master()


# 七。super（）调用父类的方法

# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子配方]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
#
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[黑马煎饼方法]'
#     def make(self):
#         print(f'运用{self.kongfu},制作煎饼果子')
#
#
#
#
# class Tom(Master,School):
#     def __init__(self):
#         self.kongfu = '[独创煎饼方法]'
#     def make(self):
#         self.__init__()         # 加自己的初始化的原因：如果不加这kongfu属性值是上一次init内kongfu属性的值
#         print(f'运用{self.kongfu},制作煎饼果子')
#         #子类调用父类的同名方法和属性：把父亲的同名属性和方法再次封装
#     def make_for_master(self):
#         #父类名.函数（）
#         Master.__init__(self)   #要在次调用初始化：因为想要调用的父类的属性和方法，而属性在init的初始化位置中，所以要再次的调用
#         Master.make(self)       #注意不要忘记位置参数
#     def make_for_school(self):
#         School.__init__(self)
#         School.make(self)
#     #需求：一次调用父类（Master，School）的方法
#     def make_old_for_me(self):
#         #方法一：缺点如果定义的类名被修改，这里的也要修改，若代码量过大，十分的麻烦
#         # Master.__init__(self)
#         # Master.make(self)
#         # School.__init__(self)
#         # School.make(self)
#         #方法二。super（）方法：super（当前类名，self）.函数（）
#
#
#
#
# me = Tom()
# me.make_old_for_me()







