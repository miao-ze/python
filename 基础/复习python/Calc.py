"""
模块名称:Calc.py
功能：可以实现加、减、乘、除、整除、幂运算
作者：缪
版本：1.0
联系方式：wyys22@qq.com
完成时间:2026-08-01
"""


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return '被除数不可为0'
    return a/b
def pow(a,b):
    return a**b
def exactly_divisible(a,b):
    if b == 0:
        return '被除数不可为0'
    return a // b

Operator = ['+','-','*','/','**','//']
def Calculator(a,f,b):
    result = None
    if f in Operator:
        if f == '+':
            result = add(a,b)
        elif f == '-':
            result = sub(a,b)
        elif f == '*':
            result = mul(a,b)
        elif f == '/':
            result = div(a,b)
        elif f == '**':
            result = pow(a,b)
        elif f == '//':
            result = exactly_divisible(a,b)
        return f'{a} {f} {b} = {result}'
    else:
        return '计算符号错误'

def is_prime(num):
    if num == 1 or num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True




if __name__ == '__main__':

    a = eval(input('a: '))
    f = input('计算符号: ')
    b = eval(input('b: '))
    print(Calculator(a,f,b))


















