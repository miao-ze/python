import math
import random
import string

#
# a = 'abcdefg'
# print(a.index('g'))
#



#
# r = range(10)
# print(*r)
# print(r[3])

# 实例5.1 索引方法实现百分制转五分制
# while True:
#     score = eval(input('得分: '))
#     result = 'EEEEEEDCBAA'
#     level = score // 10
#     print(result[level])
#

# 实例5.2 判断回文字符串
# str_1 = input(': ')
# print('True') if str_1 == str_1[::-1] else print('False')


# ls = [[]]
# ls[0].append(1)
# print(ls)

# 实例5.3 输出身份证信息
# num = input('身份证: ')
# if len(num) != 18:
#     print('错误')
# else:
#     year = num[6:10]
#     month = num[10:12]
#     day = num[12:14]
#     print('出生时间是:'+year+'年'+month+'月'+day+'日')



# 实例5.4 约瑟夫环问题

# num_list = list(range(1,12))
# while len(num_list) >=3:
#     print(num_list[2],end=' ')
#     num_list = num_list[3:] + num_list[:3-1]
#     print(num_list)



# 5.5 温度转换

# temperature = input('温度:')
# if temperature[-1] in 'Cc':
#     result = float(temperature[:-1]) * 1.8 + 32
#     print('{:.2f}华氏摄氏度'.format(result))
# elif temperature[-1] in 'Ff':
#     result = (float(temperature[:-1]) - 32) / 1.8
#     print('{:.2f}摄氏度'.format(result))
# else:
#     print('输入错误')



# 实例5.7 字符串加密
# import string
# import copy
# str = input('要加密的密码:')
# gai = copy.copy(str)
# yuan_si = string.ascii_uppercase
# xiu_gai = string.ascii_uppercase[4:] + string.ascii_uppercase[:4]
#
# result = ''
# for i in str:
#     if i in yuan_si:
#         yuan = yuan_si.index(i)
#         xiu = xiu_gai[yuan]
#         result = result + xiu
#     else:
#         result = result + i
#
# print(result)


# 实例5.8 便利输出文件
#
# with open('静夜思.txt',encoding='utf-8') as file:
#     for line in file:
#         # print(line,end='')
#         print(line.replace('\n',' '))


# 实例5.9 隐私信息处理
#
# num = '13879309798'
# num_tou = num[:3]
# result = num_tou + '****' + num[-4:]
# print(result)
#

# list1 = ['ss',13,{'name':'泽平'}]
# list2 = 10
#
# str1 = '这是一个列表：{:b}'.format(list2)
# print(str1)
# print(f'列表1：{list1}')

#
# s = 'abcd'
# print(random.choice(s))


# 实例5.11 猜数游戏

# random.seed(10)
# num = random.randint(1, 128)
#
# result = 1
# while result <= 7:
#     player = int(input('猜数字：'))
#     if player > num:
#         print('大了')
#         result = result + 1
#     elif player < num:
#         print('小了')
#         result = result + 1
#     else:
#         print('猜对了！')
#         break
# else:
#     print('尝试次数过多')


# 实例5.12 模拟校验验证码

# small = string.ascii_lowercase
# big = string.ascii_uppercase
# small_and_big = string.ascii_letters
#
# code = random.sample(small_and_big,4)
# Verification_code = ''.join(code)
# print(Verification_code)
#
# player = input('验证码：')
#
# if player == Verification_code.lower() or player == Verification_code.upper():
#     print('成功')
# else:
#     print('失败')



# 实例 5.13 模拟微软序列号

# list1 = ['B','C','E','F','G','H','J','K','M','P','Q','R','T','V','W','X','Y','2','3','4','6','7','8','9']
# result = ''
# for i in range(5):
#     result += ''.join(random.sample(list1,5))
#     if i < 4:
#         result += '-'
# print(result)


# 本章练习



# （3）
# english_str = 'what you name?my name is <Miao>.'
# symbol_list = string.punctuation
# result = 0
# for i in english_str:
#     if i not in symbol_list and i != ' ':
#         result = result + 1
# print(result)


# (4)
# result = None
# num1 = input('num: ')
# if num1[-1] != '0':
#     result = num1
# else:
#     str_len = len(num1)
#     for i in range(1,str_len+1):
#         if num1[-i] == '0':
#             continue
#         else:
#             result = num1[-(str_len):1-i]
#             break
# print(result)


# (5)
# n = input('n:')
# if len(n) < 6:
#     print('输入错误')
























