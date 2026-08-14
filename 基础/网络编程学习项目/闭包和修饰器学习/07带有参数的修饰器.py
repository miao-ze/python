
'''
# 设置装饰器
def decorate(func):
    def inner(num1,num2):
        print('正在进行加法运算.....')
        print('正在进行减法运算.....')
        result = func(num1,num2)
        return result
    return inner

@ decorate
# 定义一个加法函数
def add_num(num1,num2):
    result = num1 + num2
    return f'计算结果为{result}'
@ decorate
# 定义一个减法函数
def jian_num(num1,num2):
    result = num1 - num2
    return f'计算结果为{result}'

# 此时会打印两个，但是需求是加法时打印加法运算，减法时打印减法运算
print(add_num(1,2))
# 解决方法是，定义一个函数，将修饰器封装到函数中
'''


# 设计函数，把装饰器封装到函数中
def make_strat(flag):
    # 设置装饰器
    def decorate(func):
        def inner(num1,num2):
            if flag == "+":
                print('正在进行加法运算.....')
            elif flag == "-":
                print('正在进行减法运算.....')
            result = func(num1,num2)
            return result
        return inner

    # 返回的是装饰器
    return decorate

#在这个函数中传入要进行判断的参数 再通过 @decorate 来进行修饰
@ make_strat('+')
# 定义一个加法函数
def add_num(num1,num2):
    result = num1 + num2
    return f'计算结果为{result}'
@ make_strat('-')
# 定义一个减法函数
def jian_num(num1,num2):
    result = num1 - num2
    return f'计算结果为{result}'

# 此时会打印两个，但是需求是加法时打印加法运算，减法时打印减法运算
print(add_num(1,2))
print(jian_num(4,3))