# a = input('明天的天气是：')
# if a == 'sunny':
#     print('go to school')
# else:
#     print('go to bed')
#
#
#
#                                               简单的if句型
# if True:
#     print('1')
#     print('2')
# print('3')
#
# if False:
#     print('1')
#     print('2')
# #注意:如果条件成立只执行带缩进的代码,不带缩进的代码不属于if的语句块
# print('3') # 这个不在if语句
#
# #                             1.简单的if语句(去上学）
# weather = 'sunny'
# if weather == 'sunny':
#     print('go to school')
#
# #                           2.if-else语法（上网年龄）
# age = input('please input you age : ')
# if age >= '18':
#     print('you can surf thr Inter')
# else:
#     print('you can"t surf the Inter')
# #错误输入
# age = input('please input you age : ')
# if age >= '18':              #注意input接受到的数据类型是str（字符串），所以无法和18这个整型输出，所以18要加上引号
#     print('you can surf thr Inter')
# else:
#     print('you can"t surf the Inter')
# #1.也可以用f'{}'格式进行转化，如
# age = input('please input you age : ')
# if age >= f'{18}':
#     print('you can surf thr Inter')
# else:
#     print('you can"t surf the Inter')
# #2.也可以转换为整型如在input前加上int
# age = int(input('please input you age : '))
# if age >= 18:
#     print('you can surf thr Inter')
# else:
#     print('you can"t surf the Inter')

#                                   3.多重判断（if-elif-else）
# 1.#有问题当age>99时无法打印出else
# age = input('please input you age : ')
# if age < '18':
#     print(f'your age are {age}',',not in conformity with the law',',you are child labor')
# elif (age >= '18' and age <= '60'):
#     print(f'you age are {age}',',conformity the law',',you are wolker')
# elif age > '60':
#     print(f'you age are {age}',',you can retire')
# else:
#     print('you nor huminty')
# # 2.
# age = int(input('please input you age : '))
# if age < 18:
#         print(f'your age are {age}', ',not in conformity with the law', ',you are child labor')
# elif (age >= 18 and age <= 60):   #也可以写成这个方式：else 18 <= age <= 60
#         print(f'you age are {age}', ',conformity the law', ',you are wolker')
# elif age > 60:
#         print(f'you age are {age}', ',you can retire')
# else:
#         print('you nor huminty')
#
# #                               3.if嵌套（例子：坐公交车）
# money = float(input('请输入您的余额：'))
# if money > 0:
#     print('请上车')
#     seat = (input('看是否有位子：'))
#     if seat == '有':
#         print('可以坐下来')
#     else:
#         print('站着')
# # 高级点的
# money = float(input('请输入您的余额：'))
# if money >= 1:
#     print('请上车')
#     seat = (input('看是否有位子：'))
#     if seat == '有':
#         print('可以坐下来')
#     else:
#         print('站着')
# else:
#     print('观察司机是否注意自己')
#     see = input('可不可以溜进去：')
#     if see == '可以':
#         print('溜进去')
#     else:
#         print('放弃霸王车')

# #2.三目运算符 （用于简单的if语句）
# 语法     条件成立的表达式 if 条件 else 条件不成立的表达式
# #例子
# a = 1
# b = 2
# c = a if a > b else b
# print(c)
##高阶的的
# a = 1
# b = 2
# c = a -b if a > b else b + a
# print(c)