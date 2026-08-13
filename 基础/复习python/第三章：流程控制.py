import math
# a = 10
# b = 2 * 5
# print(a is b)

# 实例3.1 兔子繁衍问题
# result = 0
# start1 = 0
# start2 = 1
# month = int(input('月份：'))
#
# if month >= 1:
#     print(f'{start2}月：{start2}对')
# for i in range(2,month+1):
#     result = start1 + start2
#     print(f'{i}月：{result}对')
#     start1 = start2
#     start2 = result

# 实例3.2 输出乘法表
# for x in range(1,10):
#     print()
#     for y in range(1,x+1):
#         print(f'{x} * {y} = {x*y}',end='\t')

# 实例3.3 百钱买百鸡
# total = 100
# big = 5
# medium = 3
# small = 1/3
#
# print(small)
# for x in range(1,21):
#     for y in range(1,33):
#         for z in range(1,301):
#             if (big * x + medium * y + small * z) == total and (x + y + z) == total:
#                 print(x,y,z)

# 实例3.4 计算圆周率
# a = 1
# n = 0
# result = 0
# while abs(1/a) > 1e-7:
#
#     result += 1/a * (-1) ** n
#     n += 1
#     a += 2
# print(result * 4)

# 实例3.5 百分制分数转成五分值
# score = int(input('分数：'))
# if score >= 90 and score <= 100:
#     print('A')
# elif score >= 80 and score < 90:
#     print('B')
# elif score >= 70 and score < 80:
#     print('C')
# elif score >= 60 and score < 70:
#     print('D')
# elif score >= 0 and score < 60:
#     print('F')
# else:
#     print('Date error!')

# 实例3.6 输出与3无关的数

# for i in range(1,40):
#     if i % 3 == 0 or i // 10 == 3 or i % 10 == 3:
#         continue
#     else:
#         print(i)

# 实例3.7 自身以外的最大因数
# result = None
# num = int(input('number:'))
# for i in range(1,num):
#     if num % i == 0:
#         result = i
# print(result)


# 实例3.8 判断素数
# for i in range(3,50):
#     for n in range(2,i):
#         if i % n == 0:
#             print(i,'不是素数')
#             break
#     else:
#         print(i,'是素数')

# 实例3.9 百钱买百鸡进阶
# from math import ceil
# money = int(input('钱总数：'))
# total_num = int(input('鸡总数：'))
# result = True
#
# for x in range(0,ceil(money/5)):
#     for y in range(0,ceil(money/3)):
#         z = total_num - x -y
#         if z < 0:
#             continue
#         if 15 * x + 9 * y + z == 3 * money:
#             print(x,y,z)
#             result = False
# if result:
#     print('无解')

# 实例3.10 最小公倍数
# n = int(input('正整数：'))
#
# for i in range(1,n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#         result = False
#         break
# else:
#     print('n以内没有3和5的公倍数')


# 实例3.11 最大素数
# num = int(input('n:'))
# for i in range(num,1,-1):
#     for n in range(2,i):
#         if i % n == 0:
#             break
#     else:
#         print(i)
#         break




# 本章练习（1）
# n = input('n: ')
# count = 0
# try:
#     num = int(n)
#     while True:
#         if num < 0:
#             print('error')
#             break
#         if num == 1:
#             break
#         if num % 2 == 0:
#             print(f'{num}/{2}={num / 2}',end=' ')
#             num /= 2
#             count += 1
#         else:
#             print(f'{num}*{3}+{1}={num * 3 + 1}',end=' ')
#             num = num * 3 + 1
#             count += 1
# except ValueError:
#     print('error')
# print()
# print('循环总次数：',count)


# (2)
# for i in range(1000):
#     num = str(i)
#     while len(num) < 3:
#         num = '0' + num
#     str_num = num
#     int_num = int(num)
#     if int(str_num[0]) ** 3 + int(str_num[1]) ** 3 + int(str_num[2]) ** 3 == int_num:
#         print(i,end=' ')


# (3)
# n = int(input('n:'))
# feng_zi = 1
# feng_mu = 0
# t1 = 1
# t2 = 1
# result = 0
# for i in range(2,n+1):
#     if n == 1:
#         print('{:.6f}'.format(1))
#         break
#     elif i%2 == 0:
#         feng_mu = t1 + t2
#         t1 = t2
#         t2 = feng_mu
#
#         result -= feng_zi/feng_mu
#
#         feng_zi += 1
#     else:
#         feng_mu = t1 + t2
#         t1 = t2
#         t2 = feng_mu
#
#         result += feng_zi/feng_mu
#
#         feng_zi += 1
# print('{:.6f}'.format(result + 1))
#
#
# # 初始化
# n = int(input("n:"))
# # 初始化
# total = 0
# a, b = 1, 2   # 斐波那契初始分母：第1项分母1，第2项分母2
# for k in range(1, n+1):
#     if k == 1:
#         item = 1 / a
#     else:
#         numerator = k - 1
#         # 偶数项负，奇数项正
#         if k % 2 == 0:
#             item = - numerator / b
#         else:
#             item = numerator / b
#         # 更新斐波那契分母
#         a, b = b, a + b
#     total += item
#
# print("{:.6f}".format(total))


# (4)
# from math import pi
# while True:
#     result = 0
#     a = eval(input('a:(单位pi) '))
#     b = eval(input('b:(单位pi) '))
#     a = a * pi
#     b = b * pi
#     weight = abs(a - b)
#     n = int(input('分割段数：'))
#     x = weight / n
#     for i in range(n):
#         x1 = a + i * n
#         x2 = a + (i+1) * n
#         y1 = math.sin(x1)
#         y2 = math.sin(x2)
#         result += (abs(y1) + abs(y2)) * x / 2
#     print(result)


# (5)
# n = float(input('n: '))
# zi = 1
# mu = 1
# e = 0
# while True:
#     if zi/math.factorial(mu) < n:
#         print(e)
#         break
#     e += zi/math.factorial(mu)
#     mu += 1


# (6)
a=1
b=1
mouth = int(input('月数：'))
if mouth!=1:
    for i in range(mouth-1):
        a,b = a+b,a
    print(b, '只')
else:
    print(1,'只')



# (7)
# while True:
#     km = int(input('车程：'))
#     time1 = int(input('等待时间：'))
#     cost = 0
#     if km <= 3:
#         cost += 13
#     elif km <= 15:
#         cost += 13 + (km -3)*2.3
#     elif km > 15:
#         cost += 13 + 12 * 2.3 + (km - 15) * (2.3*1.5)
#     cost += time1
#     print(round(cost,2))

















