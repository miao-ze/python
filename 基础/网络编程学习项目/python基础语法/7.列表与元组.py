# # 列表的简单体验
# animal = ['大象','狮子','snake','tiger']
# mul = [1,2,3,4,5]
# print(animal)
# print(mul)


# 一。查找
# # **列表中也有索引(下标）可以进行查找
# print(animal[0])
# print(animal[1])
# print(animal[2])
# print(animal[3])


# 二。函数
# index()   count()   len()
# name_list1 = ['tom','lily','boluo']

# 1.index()
# print(name_list1.index('lily'))
# print(name_list1.index('lilya'))     #列表中没有则会报错

# 2.count()
# print(name_list1.count('tom'))
# print(name_list1.count('toma'))      #列表中没有则会返还0

# 3.len()---统计列表中元素的个数
# print(len(name_list1))

# 三。判断是否存在
# # in     和     not in
# mul_list = [1,2,3,4,5]
# # 1，in
# print(1 in mul_list)                #返还Ture
# print(0 in mul_list)                #返还False

# # 2. not in
# print(1 not in mul_list)            #返还False
# print(0 not in mul_list)            #返还Ture


# ***小练习（查找用户输入的用户名是否已经存在
# name_list2 = ['和真','486','优优']
# you_name = input('请输入您的用户名：')
# if you_name in name_list2:
#     print(f'您输入的名字是{you_name}，已存在注册')
# else:
#     print('您输入的名字未被注册，请重新输入。')


# 四。增加数据
# append()    extend()    insert()
# name_list3 = ['伦太郎','和泉纱雾','珂朵莉']
# # 1.append()--列表序列.append（数据）      *在结尾添加
# name_list3.append('小埋')
# print(name_list3)
# name_list3.append([11,22])            #也可添加序列但与extend的添加不同
# print(name_list3)
# # 2.extend()---如果数据是个序列，则将这个序列的数据逐个添加到列表中
# name_list3.extend('xiaoming')         #xiaoming是被逐个裁开然后组合的
# print(name_list3)
# name_list3.extend(['唐亚','骨王'])      #和append的不同
# print(name_list3)
# 3.insert（）--指点位置添加
# name_list3.insert(1,'弘濑希')
# print(name_list3)

# 五。删除元素
# del 目标    pop（）   removed()   clear（）
# name_list4 = ['萌王','芙利连','辛美尔']
# 1。del
# del name_list4                    #全删除
# print(name_list4)
# del name_list4[0]                 #删指定下标，如果不指定下标则删除最后一个数据
# print(name_list4)

# 2.pop（）   可以返还被删的数据
# name_list4.pop(1)
# print(name_list4)
# a = name_list4.pop(1)               #被反还了
# print(a)

# 3.remove()--移除某个数据
# name_list4.remove('辛美尔')
# print(name_list4)

# 4.clear()--清空列表
# name_list4.clear()
# print(name_list4)


# 六。修改
# 逆置reverse（）        排序sort（）
# name_list5 = ['阿拉丁','阿里巴巴','我妻由乃']

# 1.修改指定小表的数据
# name_list5[0] = '小波奇'
# print(name_list5)
# 2.reverse(逆置）
# name_list5.reverse()
# print(name_list5)
# 3.sort    如升序(默认）和降序
# mul_list1 = [1,3,6,8,4,5,2]
# # mul_list1.sort()
# # print(mul_list1)
# mul_list1.sort(reverse=True)        #在此reverse表示排版规则，reverse=Ture为降序，reverse=False为升序
# print(mul_list1)

# 七。复制
# copy()
# name_list6 = ['小明','真轴','史奕珍']
# fuzhi1 = name_list6.copy()
# print(name_list6)
# print(fuzhi1)


# 八。列表的循环遍历     （依次打印列表中的各个数据）
# name_list7 = ['缪旋','缪恺','星猫']
# 1.while#
# i = 0
# while i < len(name_list7):
#     print(name_list7[i])
#     i += 1
# 2.for
# b = 0
# for a in name_list7:
#     b += 1
#     print(a)
#     print(b)
# 九。列表嵌套    （就是一个列表中包含了其他的子列表）

# name_lista = [['小明','小红','小绿'],['tom','lily','sfs'],['张三','张思','张武']]
# print(name_lista)
# #如何查找小红
# print(name_lista[0])                    #先找到第一个子列表
# print(name_lista[0][1])                 #找到这个元素在第一给子列表中的下标


# 综合应用--随机分配办公室
import random
# a = 1
# teachers = ['老一','老二','老三','老四','老五','老六','老七','老八','老九']
# offices = [[],[],[]]
# for name in teachers:
#     i = random.randint(0,2)
#     offices[i].append(name)
#     if len(offices[i]) != 2:
#         continue
# print(offices)
# b = 1
# for office in offices:
#     a = len(office)
#     print(f'办公室{b}的人数是：{a},他们的名字是：')
#     for name in office:
#         print(name)
#     b += 1


# 元组
# 一。创建元组
# b = 1,3,4,5,'sa'
# print(type(b))
# # 1.多个数据的元组
#
# i = (1,3,4)
# print(type(i))
# print(i)
# # 2.单个数据的元组
# a = (2,)
# print(type(a))
# print(a)


# 二。查找
# ti = (1,4,6,'tom','sunny')
# 1.根据下标查找
# a = ti[1]
# print(a)
# 2.运用index查找
# print(ti.index(1))
# 3.运用count统计
# print(ti.count(1))
# 4.运用len统计个数
# print(len(ti))


# t2 = (11,22,33,['tom','jiue',55])
# t2[1] = 'dsd'
# print(t2)
##元组不可被修改

# 可以修改的特殊情况
# t2 = (11,22,33,['tom','jiue',55])  #元组中列表的数据可以修改
# t2[3][0] = 'luiy'
# print(t2)
