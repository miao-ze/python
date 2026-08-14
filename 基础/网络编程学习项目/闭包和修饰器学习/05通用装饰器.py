
# --------------1.无参数无返回值 ------------

# 定义修饰器
def decorate(hanshu):
    def inner():
        print('启动装饰器！')
        hanshu()
    return inner
# 通过语法糖来进行装饰下面的函数
@ decorate  # 相当于： comment = decorate(comment)
def comment():
    print('哈哈！')
# 启动装饰对象 由于使用了语法糖 此时的comment（） 相当于在执行修饰器中的代码
comment()

# ------------2.带有参数的函数无返回值


#设置修饰器
def decorate(func):
    # 使用装饰器装饰已有函数时，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(a,b):
        print('正在计算中......')
        # 把inner中的参数a，b 传递给func ---> 即add_num()
        func(a,b)
    return inner
# 用语法糖进行装饰函数
@ decorate   #add_num = decorate(add_num)
def add_num(num1,num2):
    result = num1 + num2
    print('计算结果为：', result)

add_num(1,3)

# --------3.带有参数和返回值的函数

#设置修饰器
def decorate(func):
    # 使用装饰器装饰已有函数时，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(a,b):
        print('正在计算中......')
        # 把inner中的参数a，b 传递给func ---> 即add_num()
        # 由于有返回值，所以要接受返回值
        result1 = func(a,b)
        return result1
    return inner

# 用语法糖进行装饰函数
@ decorate   #add_num = decorate(add_num)
def add_num(num1,num2):
    result = num1 + num2
    return f'计算结果为：{result}'

print(add_num(1,3))


# -------4. 装饰带有不定长参数和返回值的函数
# 该装饰器还可以称为通用装饰器
#设置修饰器
def decorate(func):
    # 使用装饰器装饰已有函数时，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(*args,**kwargs):
        print('正在计算中......')
        # 把inner中的参数a，b 传递给func ---> 即add_num()
        # 由于有返回值，所以要接受返回值
        # *args: 把元组里面的每一个元素，按照位置参数的方式进行传参
        # **kwargs: 把字典中每一个键值对，按照关键字的方式进行传参
        result1 = func(*args,**kwargs)
        return result1
    return inner
# 用语法糖进行装饰函数
@ decorate   #add_num = decorate(add_num)
def add_num(*args,**kwargs):
    result = 0
    for i in args:
        result += i
    for i in kwargs.values():
        result += i
    return f'计算结果为：{result}'
print(add_num(1,3))






