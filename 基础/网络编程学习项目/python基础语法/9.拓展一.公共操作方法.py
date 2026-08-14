# 一。运算符
# str1 = 'aa'
# str2 = '11'
# list1 = [1,2,3]
# list2 = [4,5,6]
# tuple1 = (7,8,9)
# tuple2 = (10,11,12)
# dict1 = {'花':'flower','吃':'eat','早饭':'breakfast'}
# dict2 = {'冲突':'coflict','有名气':'fame','明星':'star'}
# 1.‘+’ 合并
# a = str1 + str2
# print(a)
# b = list1 + list2
# print(b)
# c = tuple1 + tuple2
# print(c)
# # d = dict1 + dict2        #字典不支持合并运算
# # print(d)
# # dict1.update(dict2)
# # print(dict1)

# 2.'*' 复制
# str1 = 'a'
# list1 = ['world']
# tuple = ('hello')
#
# a = str1 * 5
# print(a)
#
# b = list1 * 5
# print(b)
#
# c = tuple * 5
# print(c)

# 3. in 和 not in
# str1 = "abcd"
# list1 = [10,20,30,40]
# tuple = (100,200,300)
# dict1 = {'name':'tom','游戏':'game'}

# a = ('a' in str1)
# print(a)
# a = ('a'not in str1)
# print(a)
#
# b = (10 in list1)
# print(b)
# b = (10 not in list1)
# print(b)
#
# c = (100 in tuple)
# print(c)
# c = (100 not in tuple)
# print(c)

# d = ('name' in dict1)
# print(d)
# d = ('name' in dict1.keys())
# print(d)
# d = ('tom' in dict1.values())
# print(d)

# 4.len()
# str1 = 'abcdefg' + 'hkl'
# list1 = [10,20,30,40]
# tuple = (100,200,300)
# dict1 = {'name':'tom','游戏':'game'}

# print(len(str1))    #len()从一开始计数
# print(len(list1))
# print(len(tuple))
# print(len(dict1))

# 5.del或del（）
# del str1
# print(str1)
# del str1[0]            #此方法不可用
# del list1[1]
# print(list1)
# del(list1[0])
# print(list1)
# del(dict1['name'])
# print(dict1)

# 6.max()和min()
# str1 = 'abcdefg'
# list1 = [10,20,30,40]
# print(max(str1))
# print(min(str1))
# print(max(list1))
# print(min(list1))

# 7.range()         一般配合for循环使用
# for i in range(1,5):
#     print(i)

# 8.enumerate(可遍历的对象)      一般配合for循环使用
# list1 = ['a','b','c','d']
# print(list1)
# for i in enumerate(list1):
#     print(i)
# print(enumerate(list1))