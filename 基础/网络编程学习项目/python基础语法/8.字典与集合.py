# 一。字典的创建
# 1.有数据的字典
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# print(dict1)
# print(dict1[10])     #可以找到相应值对应的键
# 2.空子典
# dict2 = {}
# print(dict2)
# dict3 = dict()     #通过函数dict（）创建
# print(dict3)
# 3.通过”（键，值）“对构建
# dict4 = dict([('name','tom'),('hoppy','baseball'),('age',10)])
# print(dict4)
# print(type(dict4))
# 4.通过关键子 = 构建
# dict4 = dict(name = 'tom',age = 10,hoppy = 'baseball')
# print(dict4)
# 5.通过zip进行构建
# dict5 = dict(zip(['name','age','hoppy'],['tom',20,'basaball']))
# print(dict5)
# 6.zip的运用
# a = ['name','age','hoppy']
# b = ['tom',10,'basdball']
# c = zip(a,b)            #进行打包
# print(list(c))          #注意要进行数据类型的转换
# 7.使用fromkeys（）创建字典
# dict6 = dict.fromkeys(['name','age'],10)
# print(dict6)


#二。字典的常见操作

# 1.增，
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# dict1['id'] = 110           #加个键即可
# print(dict1)

# 2,删
# 2.1 del（）
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# del dict1['hoppy']
# print(dict1)
# del (dict1)     #全删了
# print(dict1)

# 2.2 clear()
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# dict1.clear()
# print(dict1)

# 2，3 pop（） 可以返还被删除的键的值
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# a = dict1.pop('age')
# print(dict1)
# print(a)
# print(dict1.pop('age',100))
#*popitem()  随机删除一个键值对
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# a = dict1.popitem()
# print(dict1)
# print(a)

# 3.修改
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,10:'aaaa'}
# dict1['name'] = 'liuy'
# print(dict1)

# 4.查找
# 4.1通过下标进行查找
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,100:'aaaa'}
# print(dict1['age'])
# print(dict1['aaa'])    #找不存在的键时会报错

# 4.2通过get（）
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,100:'aaaa'}
# a = dict1.get('naaaa',233)
# print(a)

# 4.3通过keys（）   用于查找字典中的键
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,100:'aaaa'}
# b = dict1.keys()
# print(b)

# 4.4values()     用于查找字典中的值
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,100:'aaaa'}
# c = dict1.values()
# print(c)

# 4.5 items()      查找键值对
# dict1 = {'name': 'tom','hoppy':'baseball','age':10,100:'aaaa'}
# d = dict1.items()
# print(d)

# 小练习---创建英文字典
# 1。1
# dict_a = {'卷心菜':'cabbage','图书馆':'library','天空':'sky'}
# a = input('请输入想要查找的单词：')
# print(dict_a[a])
# 1.2
# chinese = ['核心','弄脏','控制盘']
# english = ['core','mess','panel']
# a = dict(zip(chinese,english))
# print(a)
# word = input('请输入想要查找的单词：')
# print(a[word])
# 2更新英文字典
# dict1 = dict(name = 'tom',age = 10,hoppy = 'baseball')
# del dict1['name']
# print(dict1)
# dict1.update({'name':'lily','age':20})
# print(dict1)
# dict1['hoppy'] = ['pipong','volually']
# print(dict1)

# 5.复制
# import copy
# dict1 = {'卷心菜':'cabbage','图书馆':'library','天空':['sky','tiankong']}
# dict2 = dict1
# dict3 = dict1.copy()                #浅复制
# dict4 = copy.deepcopy(dict1)        #深复制*记得导入模板
#
#
# dict1['卷心菜'] = '白菜'
# dict1['天空'].remove('tiankong')
#
#
# print(dict1)
# print(dict2)
# print(dict3)
# print(dict4)


# 三。字典的遍历
# 1.keys（）
# dict1 = {'卷心菜':'cabbage','图书馆':'library','天空':['sky','tiankong']}
# a = dict1.keys()
# print(a)
# for i in a:
#     print(i)

# 2.values()
# dict1 = {'卷心菜':'cabbage','图书馆':'library','天空':['sky','tiankong']}
# b = dict1.values()
# print(b)
# for o in b:
#     print(o)

# 3.items()
# dict1 = {'卷心菜':'cabbage','图书馆':'library','天空':['sky','tiankong']}
# print(dict1)
# c = dict1.items()
# print(c)
# for d in c:
#     print(d)
# *3. items的拆包
# dict1 = {'卷心菜':'cabbage','图书馆':'library','天空':['sky','tiankong']}
# c = dict1.items()
# for key,valus in c:
#     # print(key)
#     # print(valus)
#     print(f'{key}={valus}')



# 集合
# 一.集合的创建
# s1 = {10,20,30,40,50,12}
# print(s1)
#
# s2 = {10,10,10,20,30,40}        #集合有去重复的作用
# print(s2)

# 运用 set（）函数创建集合    set()函数可以把其他类型的数据转换为集合
# s3 = set('123456789')
# print(s3)
# 进行数据类型的转换
# s4 = set([1,2,3,4,5,6,2,3,4])
# print(s4)
# 2.创建新集合
# a = set()
# print(a)

import copy


# 二。集合的常见操作方法
# 1.add()               添加单个数据
# s1 = {10,20,30,40,'tom','sunny'}
# s1.add(10)
# print(s1)

# 2.update()            添加一个集合
# s1 = {1,10,20,}
# s2 = set('猪马炮1')
#
# s1.update(s2)
# print(s1)
# s1.update([50,60,70])
# print(s1)

# 3.remove()           删除数据
# s1 = {10,20,30,40,'tom','sunny'}
# s1.remove(10)
# print(s1)
# s1.remove(100)
# print(s1)

# 4.discard()
#   -----------------用法和remove一样，不同在于若数据不存在时不会报错

# 5.pop（）       随机删除一个数据，并返回这个数据
# s1 = {10,20,30,40,'tom','sunny'}
# b = s1.pop()
# print(s1)
# print(b)

# 6.clear()
# s1 = {10,20,30,40,'tom','sunny'}
# s1.clear()
# print(s1)

# 三。查找
#
# s1 = {10,20,30,40}
# print(10 in s1)             #in 判断数据在集合中
# print(50 not in s1)         #not in 判断数据不在集合中

# 四。集合运算
# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a & b)    #交集
# print(a | b)    #并集
# print(a - b)    #差集
# print(a ^ b)    #补集
# print(a >= b)
# print(a >= b)
