
'''
# 定义一个类
class A(object):
    name = "姓名"
    class_id = '班级编号'
    # __cal__ 方法可以使实例对象直接调用函数
    def __call__(self, *args, **kwargs):
        print(f'请输入你的{self.name}，和{self.class_id}')
        print('要下课了')
    def speak(self):
        print('要下课了')
# 用类创建对象
a = A()
# 如果没有__call__ 方法，就不可以进行实例对象的直接调用
a()
a.speak()
'''

class AAA(object):
    def __init__(self,func):
        self.__func = func
    def __call__(self, *args, **kwargs):
        print('时间快到了')
        # 调用实例对象
        self.__func()

@ AAA  #----> comment = AAA(comment)
# 因为AAA 是类，再类中又用了__init__来初始化实例，
# 且comment函数作为参数，实例化了，所以再__call__方法中可以直接进行调用
def comment():
    print('要下课了！')
comment()