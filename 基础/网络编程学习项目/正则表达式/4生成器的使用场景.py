"""用生成器生成斐波那契数列"""
# num 表示要生成数据的个数
def feibonaqi(num):
    # 进行初始化
    a = 0
    b = 1
    # 定义用来记录生成数据的个数
    current_num = 0
    while current_num < num:
        # 用来设置取到的第一个值
        result = a
        #条件成立时，交换两个变量的值
        a,b =b,a+b
        current_num += 1
        yield result
# 创建生成器
f = feibonaqi(6)
for value in f:
    print(value)

