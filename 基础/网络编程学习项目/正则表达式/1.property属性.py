
"""property属性的介绍：
1作用.就是负责把一个方法可以当作属性进行使用，以此简化代码
2.定义property属性有两种方式：修饰器方法、类属性方法
"""



'''1.修饰器方法'''
class Student(object):
    def __init__(self):
        # 1.设置私有属性
        self.__age = 0
        # 2.设置公共方法来访问私有属性
    def age(self):
        return self.__age

student =Student()
# 现在是调用方法的形式，获取属性，现在设置property属性把方法设置成属性
age = student.age()
print(age)


# 设置property属性
class Student(object):
    def __init__(self):
        # 1.设置私有属性
        self.__age = 0
        # 2.设置公共方法来访问私有属性
    @property # 当调用property属性时会执行下面的方法
    def age(self):
        print("获取属性成功")
        return self.__age

    # 3.现在设置私用属性，那同样要制作一个方法，但这个方法要和获取的方法名一样
    @ age.setter # 【当调用对象age属性设置值时会调用下面方法】
                 #  注意：使用修饰器方法的方式，方法名要保持一致
    def age(self,new_age):
        print('设置属性值')
        # 对设置属性值的正确性进行判断
        self.__age = new_age
student =Student()
# 当获取属性时，会执行property下方修饰的方法
age = student.age
print(age)
# 设置属性
student1 = Student()
student1.age = 30
print(student1.age)


'''2.类方法的使用'''
class Student(object):
    def __init__(self):
        # 1.设置私有属性
        self.__age = 0

    def get_age(self):
        print("获取属性成功")
        return self.__age

    def set_age(self,new_age):
        print('设置属性值')
        # 对设置属性值的正确性进行判断
        self.__age = new_age
    # 用property关联获取、设置方法，让age可以像普通属性一样访问
    # 1.get_age 表示获取age属性的时候执行
    # 2.set_age 表示设置age属性的时候执行
    age = property(get_age,set_age)

# 进行属性的获取
student1 = Student()
print(student1.age)
# 进行属性的设置
student2 =Student()
student2.age = 30
print(student2.age)
