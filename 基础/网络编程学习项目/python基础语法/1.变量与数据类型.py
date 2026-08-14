
# 1.警号:   #                 （用于单行）
# 2.三引号 ’‘’ ‘’‘ 或 ”“” “”“ （用于多行注释）
# 注释用于对代码进行解释说明
#                                                                             变量
# 语法： 变量名 = 值 （相当于赋值）要满足标识符的命名规则
# 1.1由数字，字母，下划线组成
# 1.2不能数字开头
# 1.3不可使用内置关键词
# 1.4严格区分大小写

# 命名习惯
# 2.1大驼峰 如Mymane
# 2.2小驼峰 如myMane
# 2.3下划线 如my_mane

#                                                             使用变量
# my_mane = "TOM" # TOM是单词需用引号
# print(my_mane)
# shool_name = "黑马程序员"
# print(shool_name) # 代码是自上而下运行的
# 数据类型  可用type进行检查，但记得打print（打印）字符
# 数值：int（整形） float（浮点型）
# 布尔型：True（真(1)） False（假(0)）
# str（字符串）  list（列表）  tuple（元组）  色图（集合）  dict（字典）
# a = 1
# b = 1.1
# c = "me"
# print(type(a))
# print(type(b))   #用于查看类型
# print(type(c))
# d = [1,2,3]
# print(type(d)) # 列表
# e = (1,2,3)
# print(type(e)) # 元组
# f = {"name":'TOM','age':18} # 字典
# print(type(f))



#                                                         格式化输出
# 格式符号
# 常用：%s(字符串)   %d（有富豪的十进制整数）   %f（浮点数）  其他的可以自己去查

# age = 8
# name = 'TOM'
# print('我今年%d岁了' % age)
# 输出多个时
# print('我的名字时%s,我今年%d岁了' %(name,age))
# print('我的名字时%s,我明年%d岁了' %(name,age + 1)) #运用+符号
# 拓展  可以都用字符串类型 即%s十分强大
# print('我的名字时%s,我明年%s岁了' % (name,age))
# print(f'我的名字是{name},我明年{age}岁了')          # f格式：f'{}'
# s = '我的名字是{},我的工资是{}元'.format('缪紫',1233)  #fotmat()方法
# print(s)
# a = '我的名字是{1},我的工资是{0}元'.format('缪紫',1233)
# print(a)
#                                                       转义字符篇
# 1.\n 转行符
# a = '我的名字是缪泽平\n来自数字经济3班'
# print(a)
# 2.\t 制表符
# a = '网名\t\t\t\t\t\t域名\t\t\t\t\t\t\t\t年龄\t\t价值'
# b = '失落的小站\t\t\t\thttps://www.shinnku.org/\t\t19\t\t10000w'
# c = '烟虑频道\t\t\t\t\thttps://yanyugal.top/\t\t\t20\t\t20002w'
# print(a)
# print(b)
# print(c)
# 3.\'  单引号符
# print("we\' are friend")
# print("we\' are friend")
# 4.\\' 反斜杠符号
# print("we\\' are friend)
#
# 结束符 end=  在python中print自带end='\n'
# print('hello',end='\n')
# print('hello',end='\t')



