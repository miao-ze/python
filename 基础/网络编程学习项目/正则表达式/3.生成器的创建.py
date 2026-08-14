"""
生成器：就是根据程序员指定的算法循环生成数据，条件不成立时结束执行
特点：不是一次性全部生成数据，使用一个生成一个，可以节省内存资源
有两种创建方式： 1.生成器推导式     2。使用yield关键字
"""


'''(一)：生成器推导式'''
# 就是把列表推导式中的中括号改成小括号
generator1 = (value * 2 for value in range(4))
print(generator1)

# 方式一：取值
# 使用生成器取值的方法：用next函数获取生成器的值
# 器取值是一个一个去的，
value1 = next(generator1)
print(value1)
value1 = next(generator1)
print(value1)
value1 = next(generator1)
print(value1)
value1 = next(generator1)
print(value1)
# 当生成器没有值可以取时，会报错

# 方式二：取值
while True:
    try:
        value2 = next(generator1)
        print(value2)
    except Exception as e:
        print('取值完毕')
        break

# 方式三：取值(体现了for循环的强大)
# for循环内部循环调用next函数获取生成器中的下一个值，当出现异常时for循环内部自动进行异常捕获
for i in generator1:
    print(i)


'''(二)：在函数中使用yield关键字，这时就不是函数，而是生成器'''
def generator2():
    for date in range(4):
        print('开始执行生成器')
        # 使用yield关键字 特点：当程序执行到yield关键字的时候代码会暂停并把结果返回，
        # 再次启动生成器时，会在暂停的位置继续往下执行
        yield date
        print('上一次数据生成完了')

result = generator2()
# value = next(result)
# print(value)
# value = next(result)
# print(value)
for i in result:
    print(i)