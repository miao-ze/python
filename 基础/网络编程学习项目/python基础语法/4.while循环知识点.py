# while是循环语句
# 此为简单的模块：
# 此为简单的模块：while 条件:
#                  条件成立重复执行的代码1
#                  条件成立重复执行的代码2

# 简单的体验
# i = 0               #先赋个值           计算机计数是从o开始的
# while i < 5:        #控制循环的范围      （结束值是5）
#     print('tom')    #要执行的命令
#     i += 1          #i += 1 相当于 i = i + 1  由于要加5次才等于5所以要循环5次   ***（增量是1）
# print('jirkr')

# 应用1 (1~~~100的累加和)
# a = 1
# result = 0
# while a <= 100:
#      result += a    #result = result + a
#      a += 1         #a = a + 1
# print(result)


# *** （注意：循序不要搞错循序)
# 应用2 （1~~~100的偶数累加和）
# 方法1  (我的方法）
# a = 0
# result = 0
# while a <= 100:
#     result += a
#     a += 2
# print(result)

# 方法2 （老师的方法）
# a = 1
# result = 0
# while a <= 100:
#     if a % 2 == 0:
#         result += a
#     a += 1
# print(result)


# break 和 continue
# break （即终止次循环）        continue （即退出当前一次循环继而执行下一次的循环代码）

# break 的小例子 (吃苹果）
# i = 1
# while i <= 5:
#     if i == 4:
#         print('吃饱了,不吃了')
#         break
#     print(f'吃了地{i}个苹果')
#     i += 1

# continue的小例子
# a = 1
# while a <= 5:
#     if a == 3:
#         print('吃到个虫子，这个不吃了')
#         a += 1                  # ***记住一定要修该计数器，否则会陷入死循环
#         continue
#     print(f'吃了地{a}个苹果')
#     a += 1

# while循环循环
# 简单的例子
# a = 1
# while a <= 3:
#     i = 1
#     while i <= 3:
#         print('对不起，我错了')
#         i += 1
#     print('涮碗')
#     a += 1

# # 运用

# 1.初阶版
# b = 1
# while b <= 5:
#     a = 1
#     while a <= 5:
#         print('*', end='')
#         a += 1
#     print()   #用来换行
#     b += 1

# 2.进阶版
# b = 1
# while b <= 5:
#     a = 1
#     while a <= b:   #（令a 和 b 有关联）
#         print('*', end='')
#         a += 1
#     print()   #用来换行
#     b += 1


# 打印九九乘法表
# 表达式是 X * X = X*X

# b = 1
# while b <= 9:
#     a = 1
#     while a <= b:
#         print(f'{a} * {b} = {a*b}',end='\t ')
#         a += 1
#     print()
#     b += 1


# while...else的句子
                # 语法:
                # while 条件
                #      条件成立重复执行的代码
                # else:
                #     循环正常结束之后要执行的代码
# i = 1
# while i <= 5:
#     print('对不起,我错了')
#     i += 1
# else:
#     print('原谅我了真开心')

# 2.while...break...else
# i = 1
# while i <= 5:
#     if i == 3:
#         break
#     print('对不起,我错了')
#     i += 1
# else:
#     print('原谅我了真开心')

# *****(遇到break,else后的代码也不执行)

# 3.while...continue...else
# i = 1
# while i <= 5:
#     if i == 3:
#         i += 1  #***很重要,为了改变增量,不然会进入死循环
#         continue
#     print('对不起,我错了')
#     i += 1
# else:
#     print('原谅我了真开心')


