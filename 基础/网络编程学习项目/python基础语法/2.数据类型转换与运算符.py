# 1.输出 语法：input（）  运行到input时程序会停下来
# a = input('请输入你的密码:') #一般吧input赋值即储存为变量
# print('你输入的密码是:%s' % a)
# print(type(a))
# print('你输入的密码是:%s' % a)
# 重要点：*打印的值为你输入的值，不用引号里的其他信息


# 数据类型转换
# 常用：int（）  folat（）  str（）  list（）  tuple（）  eval（）
# b = input('请输入数字：')
# print(type(b))      #转化前
# print(type(int(b))) #转化后
# c = '1'
# print(float(c))       #将1转换成浮点型
# d = '2'
# print(str(d))
# print(type(str(d)))   #将2转换成字符串
# #eval（）很方便
# print(type(eval(c)))  #用eval（）时变量值要为字符串



# 运算符
#                                 1. 算数运算符
# print(1 + 2)
#a = 1 + 1
# print(a)
# b = 1 - 1
# print(b)
# c = 2 * 2
# print(c)
# d = 4 / 2  #除法的到的结果都为小数
# print(d)
# e = 6 % 4  #取余
# print(e)
# f = 9 // 2 #整除
# print(f)
# 赋值运算符
# 多个变量赋值
# a,b,c, = 1,2,'tom'
# print(a)
# print(b)
# print(c)
# print(a,b,c)
# 多变量负相同的值
# d = e = 100
# print(d)
# print(e)
#                                   2.复合复赋值运算符
# a = 1
# a += 3
# print(a)
# a = 1
# a -= 3
# print(a)
# a = 1
# a *= 3
# print(a)
# a = 1
# a /= 3
# print(a)
# a = 1
# a %= 3
# print(a)
# a = 2
# a **= 3
# print(a)
# 小知识点     a *=b+1  相当于  a = a*(b+1)
#                                   3.关系运算符（比较运算符）所得结果是一个布尔值即Ture或flase
# a = (1 == 1)     #等于
# print(a)
# b = (1 != 2)     #不等于
# print(b)
# c,d = 3,4
# e = (c <= d)     #小于等于
# print(e)
# f = 1 >= -1       #大于等于
# print(f)
# 小点（赋值后也可以不用括号）
#                                   4.逻辑运算符:(and,or,not)
# a = 0
# b = 1
# c = 2
# and用法   都真才真
# print (b > a and c >b )
# print (b < a and c >b )
# or用法    一真则真，都假才假
# print (b < a or c < b )
# print (b < a or c > b )
# print ((b < a) or (c > b))
# not用法   取反
# print(not c > b)       #c是大于b本是真，但有not所以取反，所以输出结果为假
# 拓展                              5.数字之间的运算符

# a = 0
# b = 1
# c = 2
# print(a and b)
# print(c and b)
# print(a or b)
# print(c or b)