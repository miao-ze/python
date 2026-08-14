"""自定义上下文管理器与with语句一起配合使用：所以open函数创建的文件对象就是一个上下文管理器对象
1. 用类进行创建
一个类只要实现了__enter__()和__exit__()这两个方法，就称为上下文管理器
2. 用函数进行创建（要使用装饰器）
"""

'''一：用类进行创建'''
class File(object):
    # 因为是结合with语句使用的，所以要传入文件名，和访问模式
    def __init__(self,file_name,file_mode):
        self.file_name =file_name
        self.file_mode =file_mode
    def __enter__(self):
        # 此为上文方法：主要是提供对象资源，负责返回操作对象的资源|
        # 比如：文件对象、数据库连接对象

        self.file = open(self.file_name,self.file_mode,encoding='utf-8')
        print("文件资源以打开")
        return self.file

    # 当with语句执行完成以后自动执行__exit__方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 此为下文方法: 负责释放对象|比如：关闭文件、关闭数据库
        print('over')
        self.file.close()
# 用with语句结合用类创建的上下文管理器
with File("1.txt",'r') as file:
    file_date = file.read()
    print(file_date)



'''2.用函数创建装饰器(要导入装饰器)'''
from contextlib import contextmanager
# 加上装饰器，则下面创建的函数对象就是一个上下文管理器
@contextmanager
def my_open(file_name,file_mode):
    try:
        file = open(file_name,file_mode,encoding='utf-8')
        # yield 关键字之前的代码可以认为是 上文方法，负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        # yield 关键字之后的代码可以认为是 下文方法，负责释放对象资源
        print('over')
        file.close()
# 普通函数不可以结合with语句使用，所以到导入装饰器，对函数进行装饰
with my_open('1.txt','r') as file:
    file_date = file.read()
    print(file_date)