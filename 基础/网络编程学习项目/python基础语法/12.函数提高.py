# 一.变量的作用域
# 分为: 局部变量和全局变量
# 1.局部变量
# def tes():
#     a = 100       #次变量是定义在函数内的
#     print(a)
# tes()
# print(a)        #由于a有定义在函数内的变量100,所以在函数外访问不到,所以会报错

# 2.全局变量

# 2.1
# a = 100         #定义在全局
# def tesA():
#     print(a)
# tesA()

# 2.2 修改全局变量
# a = 100
# def tes1():
#     print(a)
# def tes2():
#     a = 200             #此处的(a=200)不是在全局中进行修改,而是在局部中定义的一个局部变量
#     print(a)
# tes1()
# tes2()
# print(a)                #(a)仍是100

# 2.3 用global进行全局变量的修改
# a = 100
# def tes1():
#     print(a)
# def tes2():
#     global a            #运用global进行声明a为全局变量
#     a = 200
#     print(a)
# tes1()
# tes2()
# print(a)                #此时(a=200),变为了全局变量.



# 二,多函数程序执行流程

#一般在实际开发中，一个程序往往由多个函数组成，并且多个函数共享某些数据
# 1.共有全局变量
# glo_num = 0
# def tes1():
#     global glo_num
#     glo_num = 100
#     print(glo_num)
# def tes2():
#     print(glo_num)
# print(glo_num)   # 0  注意此时函数内的（global）声明还没调用
# tes2()           # 0  修改的函数还没执行
# tes1()
# tes2()
# print(glo_num)   # 100 此时才被调用

# 2.返回值作为参数传递
# def tes1():
#     return 10
# def tes2(num):
#     print(num)
# result = tes1()         #保存tes1的返回值
# tes2(result)            #将tes1的返回值作为参数传递到tes2函数中



# 三。函数的返回值
# 当一个函数有多个return时，只执行第一个return的返回值，无法在一个函数中返回多个值
# def tes1():
#     return 1
#     return 2        #第二个返回值不会执行
# a = tes1()
# print(a)

# 一个函数多个返回值的方法
# def tes3():
#     return 1,3  #用逗号隔开
# a = tes3()
# print(a)        #（1，3）注意此时返回的是一个元组

# 也可以返回列表、字典
# def tes3():
#     return {'卷心菜':'cabbage','图书馆':'library','天空':'sky'}
#
# a = tes3()
# print(a)



# 四。函数的参数

#1.位置参数     (即实参与形参的位置顺序应一致）
# def i(name,age,sex):
#     print(f'您的姓名是:{name},年龄是:{age},性别是:{sex}')
# i('tom',10,'男')         #此时顺序是正确的
# i('男',10,'tom')         #此时位置是错误的

# 2.关键字参数
# def i(name,age,sex):
    # print(f'您的姓名是:{name},年龄是:{age},性别是:{sex}')
# i(age=10,sex='男',name='tom')            #运用关键字“=”来指定参数，此时不进行位置区分

# 3.缺省参数（默认参数）
# def i(name,age,sex='女'):
#     print(f'您的姓名是:{name},年龄是:{age},性别是:{sex}')
# i('tom',10)         #使用默认值
# i('tom',10,'男')

# 4。不定长参数 （也叫可变参数，用于不确定会传递多少个参数的情况）
# 4.1 包裹位置传递‘*’   返还的是元组
# def into(*arge):
#     print(arge)
#     return 35
# c = into(1,2,3,4,5)
# print(c)
# 4.2包裹关键字传递(**)  返还的是字典
# def oceanic(**kwargs):
#     print(kwargs)
# oceanic(name='tom',age= 10,hoppy='baseball')

# 五，拆包和交换变量值
# 1.1拆包:元组
# def fertile():
#     return 1,2
# c =fertile()
# num1,num2 = c
# print(num1)
# print(num2)
# 1.2拆包：字典
# def attitude():
#     return {'name':'tom','age':10}
# a,b = attitude().values()
# print(a)
# print(b)

# 2.交换变量值
# 方法一：利用第三变量
# a = 10
# b = 20
# '''要令 a = 20 , b = 10'''
# c = 0       #定义中间变量
#
# c = a       #此时 c = 10
# a = b
# b = c       #令 b = c（10）
#
# print(a)
# print(b)

# 方法二(化简写法）
# a,b =1,2
# a,b = b,a
# print('a =',a)
# print('b =',b)

# 六，引用  运用id（）函数
# 1.1int()类型 不可变数据类型
# a = 1
# b = a
# print(id(a))
# print(id(b))
#
# a = 2
# print(id(a))      #id值改变了,对应不可变类型

# 1.2 list（） 可变类型
# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))
#
# a.append(4)
# print(id(a))
# print(id(b))        #id值一样，为可变类型


# 2.引用当做实参
# def ironic(mul):
#     print(mul)
#     print(id(mul))
#     mul += mul
#     print(mul)
#     print(id(mul))
#
#
#
# b = 100
# ironic(b)
#
# c = [1,2,3]
# ironic(c)