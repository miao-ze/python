# 列表，字典，集合的推导式      用来化简用的
# 一；列表的推导式
# 用平常的方法进行创建
# list1 = [0,1,2,3,4,5,6,7,8,9,10]
# print(list1)

# 1.用for------------创建
# list2 = []                    #先准备一个空列表
# for i in range(11):
#     list2.append(i)
# print(list2)

# 2.用while----------创建
# a = 1
# list3 = []                      #先准备一个新列表
# while a <= 10:
#     list3.append(a)
#     a += 1
# print(list3)

# # 用列表推导式的实现
# list4 = [i for i in range(11)]
# print(list4)

# 带if的列表推导式
# 创建0-10从的偶数列表

# list3 = [i for i in range(11) if i % 2 == int()]
# print(list3)


# list1 =[i for i in range(0,11,2)]
# print(list1)

# list2 = []
# for i in range(11):
#     if i % 2 == int():
#         list2.append(i)
# print(list2)


# 多个for循环实现列表推导式

# for a in range(1,3):
#     for b in range(0,3):
#         print((a,b),end=' ')

# c = 0
# while c <= 1:
#     c += 1
#     d = 0
#     while d <= 2:
#         print((c,d),end=' ')
#         d += 1

# list4 =[(i,o)for i in range(1,3)for o in range(0,3)]
# print(list4)

# 字典的推导式

# list1 = [1,2,3]
# list2 = ['a','b','c',]
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)

# 平常的
# list3 = list1 + list2
# print(list3)
# print(list3[0])
# dict1 = dict(zip(list1,list2))
# print(dict1)
# 平常的
# list1 = []
# dict1 = {}
# for i in range(1,6):
#     list1.append(i)
# list2 = []
# for b in range(1,6):
#     b *= b
#     list2.append(b)
# dict2 = dict(zip(list1,list2))
# print(dict2)

# 化简后的推导式
# list3 = [i for i in range(11) if i % 2 == int()]
# print(list3)

# 提取字典中的目标数据
# dict1 = {'tom': 234,'liur':124,'miao':329,'id':128}
# for (key,value) in dict1.items():
#     if value >= 200:
#         print((key,value),end=' ')
# 利用推导式化简后
# dict2 = {(key,value) for (key,value) in dict1.items() if value >= 200}
# print(dict2)

# 集合推导式
# list1 = [1,2,3]
# set1 = {i ** 2 for i in list1}
# print(set1)
#
#
# a = set()
# for i in list1:
#     b = i ** 2
#     a.add(b)
# print(a)


