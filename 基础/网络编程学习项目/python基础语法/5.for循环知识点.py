# for 的语句
# for 临时变量 in 序列
#     重复执行的代码1
#     重复执行的代码2

# 快速体验
# a = 'Hello'
# for i in a:
#     print(i)

# 配合break和Continue使用

# 1.for与break与else
# a = 'Hello'
# for i in a:
#     if i == 'l':
#         break
#     print(i)

# 1.2 a = 'Hello'
# for i in a:
#     if i == 'l':
#         print('遇到l不打印')
#         break
#     print(i)
# else:
#     print('结束')


# 2.for与continue与else
# a = 'Hello'
# for i in a:
#     if i == 'l':
#         continue
#     print(i)

#2.2 a = 'Hello'
# for i in a:
#     if i == 'l':
#         print('遇到l不打印')
#         continue
#     print(i)
# else:
#     print('结束')


# *** break和continue在while和for中的作用是一样的

# 1.for...else
# a = 'Hello'
# for i in a:
#     print(i)
# else:
#     print('tom')

# a = 'Hello'
# for i in a:
#     print(i)
# else:
#     print('tom')

# for与range的使用
# for num in range(1,5):
#     print(f'{num}')

# 求累加和
# n = int(input('请输入您想要累加的个数: '))
# s = 0
# for a in range(1,n+1):
#     s += a
# print(s)

# 九九乘法表
# for b in range(1,10):
#     for a in range(1,b + 1):
#         print(f'{a} * {b} = {a*b}',end='\t')
#     print()
