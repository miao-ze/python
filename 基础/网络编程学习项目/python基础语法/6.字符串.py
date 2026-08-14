# 一。字符串常见的使用引号来定义
# # 1.1一对引号
# #单引号
# a = 'my name ' \
#     'is tom'
# print(a)
# print(type(a))
# #双引号
# a = "my name" \
#     " is tom"
# print(a)
# print(type(a))
# #三引号
# a = """my name
# is tom"""
# print(a)
# print(type(a))
# # ***（注意三引号换行输出的不同)

#I'm tom 的输入
# 1.2
# a = "I'm tom"
# print(a)
# 1.3
# b = 'I\'m tom' #加个转义符号
# print(b)

# # 二.字符串的的输出
# a = 'tom'
# print('my name is %s' % a)  # %s的输出
# print(f'my name is {a}')    # f格式的输出
#
# # 三。字符串的的输入
# password = input('请输入您的密码:')
# print(f'您输入的密码是{password}')

# #4.下表‘’索引‘’ (用来精确的找打目标）
# # 字符串在保存进内存是都被记录了下表
# a = 'abcdefg'
# #如果想只打印a这个字符串则
# print(a[0])
# #如果想只打印b这个字符串则
# print(a[1])
# # ***每个下表从前往后由0开始往后分配

# 五.切片(分片)
#截取其中一部分的操作。字符串·列表·元组都支持切片
#语法     序列[开始位置下标：结束位置下标：步长]
# str = '0123456789'
# print(str[2:5:1])                  #和print(str[2:5])结果一样
#
# str = '0123456789'
# print(str[2:5:2])
# print(str[2:5])
# print(str[:5])                     #默认从0开始选取
# print(str[2:])                     #从2开始到最后
# print(str[:])                      #选取所有

# 负数测试
# print(str[::-1])                   #倒叙选取
# print(str[-4:-1])                  #指倒数地四个数到倒数地一个数，方向为从左向右。最后一个数不选
# print(str[-4:-1:-1])               #不可选取，-1步长指从右向左选取
# print(str[-1:-4:-1])               #方向一致则可以选取

# 5.1相加与相乘
# 1.相加
# str1 = 'hello,' + 'world'
# print(str1)
# str2 = [1,2,3] + [4,5,6]
# print(str2)
# # 2.相乘
# str3 = 'tom,' * 3
# print(str3)
# 5.2计算长度、最小值和最大值            #函数为：len（）
# 1，计算长度
# str4 = 'asdfghjkl'
# print(len(str4))
# 2计算最大值和最小值                   #函数为：max（） 和 min（）
# list1 = [1,2,3,4,5,6]
# list1 = (1,2,3,4,5,6)
# print(max(list1))
# print(min(list1))

# 六.查找

# a = 'are you like me or like he you can say quilk'

# 所谓字符串的查找方法即时查找字串在字符串中的位置或出现位置
#1。find                               #检查某个字串是否在这个字符串中，如果在这返回这个字串开始的位置下标，否则则返回-1
# 语法    字符串序列.find（字串,开始位置下标,结束位置下标）
# print(a.find('like'))
# print(a.find('like',9,30))           #在第9个字串和第30个字串中查找like的位置
# print(a.find('likes'))               #如果没有则返还-1

# * print(a.find('like'))             #用法与find一样，但从右侧开始查找

#2.index()                             #与find大致相同，不同在于没有则返还报错
# print(a.index('like'))
# print(a.index('like',9,30))
# print(a.index('likes',9,30))

# print(a.rindex('like'))               #与index一样，但从右侧开始查找

#3.count                                #用于查找字串的出现个数
# print(a.count('like'))
# print(a.count('like',1,15))
# print(a.count('likes'))               #不存在的返还0


#七.修改
# a = 'are you like me or like he you can say quilk'


# 1.replace() 替换
# 语法        字符串序列.replace（旧字串，新字串，替换次数）
# print(a.replace('like','app'))
#
# a.replace('like','app')
# print(a)                               #此方法不可
#
# b = a.replace('like','app')
# print(b)                               #赋值存变量后则可以

# print(a.replace('like','app',1))
# print(a.replace('like','app',10))      #替换次数如果超出字串出现次数，表示代替所有这个字串



# 2.split() —- 分割，返还一个列表
# a = 'are you like me or like he you can say quilk'

# 语法      字符串序列.spilt(分割字符，num)    *num指分割字符出现的次数，即将来返还数据个数为num+1个。
# b = a.split('like')
# print(type(b))
        #分割后成为列表
# print(a.split('like'))
# print(a.split())                         #进行全部分割
# print(a.split(' ',2))   #以空格为分割符，分割两次

# c = a.split('like',1)
# print(c)



# 3.join() -- 合并列表里的字符串数据为一个大字符串
# 语法      连接符.join(字符串)
# 快速体验
# print('-'.join('python'))

# d = ['aa','bb','cc']
# e = '......'.join(d)
# print(e)

# 4.strip()-- 移除首尾字符   (lstrip删除字符串左侧字符，rstrip删除字符串右侧字符）

# str1 = '    are you like me or like he you can say quilk    '
# print(str1.strip('ak'))
# print(str1.strip(' '))
# print(str1.strip(' ak'))
# print(str1.lstrip(' '))
# print(str1.rstrip(' '))


# 5.判断字符种类
# 1.isalnum()--检测字符串是否由字母和数字组成，或两种中的一种，是则返回Ture，否则返回False
# str2 = 'asfasf'
# print(str2.isalnum())
# 2.isalpha()--判断都是字母
# str3 = 'abcd'
# print(str3.isalpha())
# print(str3.isdigit())

# 3.isdigit()--判断都是数字
# str4 = '1234'
# print(str4.isdigit())
# print(str4.isalpha())

# 4.isspace()--判断空白
# str5 = ' '
# print(str5.isspace())

#非重点，关于大小写转换
# 1.capitalize      将字符串中第一个字符装换成大写
# a = 'Are you like me or like he you can say Quilk'
# print(a.capitalize())
# 2.tital           将字符串中每个单词首字母转换成大写
# print(a.title())
# 3.upper           小写转大写
# print(a.upper())
# 4.lower           大写转小写
# print(a.lower())

# 八，判断      startswith() 和 endswith()
# 所谓判断即是判断真假，返回的结果是布尔型数据类型：Ture或False
# 语法     字符串.startswith(字串，开始位置下标，结束位置下标)
# mystr = 'hello workd and itcast and itheima and python'
#
#
# print(mystr.startswith('l',2,4))
# 1.startswith()  判断开头
# print(mystr.startswith('hello'))
# print(mystr.startswith('h'))
# print(mystr.startswith('h2'))
#2.endswith（）    判断结尾
# print(mystr.endswith('python'))
# print(mystr.endswith('n'))
# print(mystr.endswith('python1'))