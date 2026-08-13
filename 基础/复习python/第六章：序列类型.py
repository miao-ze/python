import math
import random
import pandas

# 实例6.1 成绩统计分析

# score = []
# with open('静夜思.txt','r',encoding='utf-8') as file:
#     for i in file:
#         a = i.strip()
#         b = a.split()
#         c = b[-1]
#         score.append(c)
# print(score)
# score_list = [94,89,96,88,92,86,69,95,78,85,100]
# num = len(score_list)
# sum_score = math.fsum(score_list)
# avg_score = sum_score/len(score_list)
# print('平均数：{:.2f} '.format(avg_score))
# score_list.sort()
# print('最高的： ',score_list[-3:])
# print('最低的： ',score_list[:3])
# if num % 2 == 0:
#     meidum = (score_list[int(num/2)] + score_list[int(num/2) - 1]) / 2
#     print('中位数： ',meidum)
# else:
#     meidum = score_list[math.floor(num//2)]
#     print('中位数： ',meidum)


# 实例6.2 二维列表的排序
# score = [
#     ['缪泽平','2402099172',89],
#     ['徐晓百','2402099182',67],
#     ['王遗风','2402099192',34],
# ]
# s = sorted(score,key=lambda x:x[1])
# print(s)


# 实例6.3 列表赋值与复制
# ls = [1,2,3,['name','缪泽平'],4]
# print(ls,id(ls))
# ls1 = ls[1:3]
# print(ls1,id(ls1))


# 实例6.3 自幂数
# n = int(input('n: '))
# num = 10 ** n
# for i in range(10 ** (n-1),num):
#     str_i = str(i)
#     len1 = len(str_i)
#     result = 0
#     # for a in str_i:
#     #     result += int(a) ** len1
#     # if result == i:
#     #     print(i)
#
#     if i == sum([int(x) ** len1 for x in str_i]):
#         print(i)




# 实例6.4 蒙特卡洛方法计算圆周率
# num = int(input('个数:'))
# n = [random.random() for x in range(num)]
# m = [random.random() for y in range(num)]
# list = zip(m,n)
# i = [(a[0] ** 2,a[1] ** 2) for a in list]
# count = 0
# for c in i:
#     if sum(c) <= 1:
#         count += 1
#
# pi = 4 * count / num
# print('{:.6f}'.format(pi))


# 实例6.5 文件中数据统计分析

# with open('静夜思.txt', 'r',encoding='utf-8') as file:
#     result = []
#     for line in file:
#         Filter_line = line.strip()
#         line_list = Filter_line.split(',')
#         list_score = line_list[-4:]
#         i = map(int, list_score)
#         avg_score = '{:.2f}'.format(sum(i)/4)
#         line_list.append(str(avg_score))
#         result.append(line_list)
#
#
# result.sort(key=lambda x:x[-1])
# print(result)
# print('平均分最高分：',result[-1][1],result[-1][-1])
# print('平均分最高分：',result[0][1],result[0][-1])
# for i in range(len(result)):
#     if i == len(result)-1:
#         print(result[i][-1], end='')
#     else:
#         print(result[i][-1], end='  ')
# print()
# name = input('姓名： ')
# for list2 in result:
#     if name in list2:
#         c = ' '.join(map(str,list2))
#         print(c)
#         break
#     else:
#         print('姓名不存在')
#         break

# 本章练习
# (1)
# factor_list = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
# check_code = [1,0,'X',9,8,7,6,5,4,3,2]
#
# result = 0
# identy_create = input('身份证：')
# identy_list = list(identy_create)
#
# if int(identy_create[6:8]) >= 5:
#     identy_list.insert(6,1)
#     identy_list.insert(7,9)
# else:
#     identy_list.insert(6,2)
#     identy_list.insert(7,0)
# for i in range(17):
#     result += int(identy_list[i]) * factor_list[i]
# remainder = result % 11
# for i in range(11):
#     if i == remainder:
#         identy_list.append(check_code[i])
# str_list = map(str, identy_list)
# str = ''.join(str_list)
# print(str)


# (2)
# a = list(map(int,input('a: ').split()))
# b = list(map(int,input('b: ').split()))
# a.extend(b)
# a.sort(reverse=True)
# print(a)

# (3)
# USER = [
#     ['aaa','123456'],
#     ['bbb','888888'],
#     ['ccc','333333'],
# ]
#
# username = input('用户名： ')
# password = input('密码： ')
# for i in USER:
#     if username in i:
#         if username == i[0] and password == i[-1]:
#             print('success')
#             break
#         else:
#             print('fail')
#             break
# else:
#     print('wrong user')



# excel_sheel1 = pandas.read_excel("C:\\Users\\Administrator\\Desktop\\手机销售数据(1).xlsx",sheet_name=0)
# excel_sheel2 = pandas.read_excel("C:\\Users\\Administrator\\Desktop\\手机销售数据(1).xlsx",sheet_name=1)
# list1 = excel_sheel1.values.tolist()
# list2 = excel_sheel2.values.tolist()
#
#
# list1_rank = sorted(list1,key=lambda x:x[1],reverse=True)
# list2_rank = sorted(list2,key=lambda x:x[1],reverse=True)
# print(list1_rank, list2_rank,sep='\n')
#
# set1 = set([phone[0] for phone in list1_rank])
# set2 = set([phone[0] for phone in list2_rank])
#
# print(set1 & set2)
# print(set1 | set2)
# print(set2 - set1)
# print(set1 ^ set2)

#
# dict1 = {'name1':1, 'name2':2, 'name3':3, 'name4':4}
# print(list(dict1.keys()))


# 实例7.3 通讯录修改
# USER = {'李明':'18434921923','缪泽平':'18379309798'}
# def modify(name):
#     for user_name in USER:
#         if user_name == name:
#             result2 = input('是否修改号码（Y）:')
#             if result2 == 'Y' or result2 == 'y':
#                 phone = input('手机号')
#                 USER[user_name] = phone
#                 return '修改成功'
#             else:
#                 return '不修改号码'
#             pass
#     else:
#         result1 = input('是否新增信息（N）:')
#         if result1 == 'N' or result1 == 'n':
#             USER.setdefault(name)
#             return '新增成功'
#         else:
#             return '不新增信息'
# if __name__ == '__main__':
#     while True:
#         name = input('姓名：')
#         a = modify(name)
#         print(a)
#


# 实例7.7 查询首都












