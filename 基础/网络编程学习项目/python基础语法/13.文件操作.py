# 文件操作包括："打开，关闭，读，写，复制等"
# 文件操作的作用是什么：“读取内容，希望如内容，备份内容等”
#
# # 一。打开 open()
# f = open('test.txt','w')
# # 2.读写操作，write()  readline()
# f.write('aaa')
# # 3.关闭 close（）
# f.close()

# 一。访问模式一
# 1,rd（只读） 如果文件不存在，报错。不支持写入到操作。
# f = open('python练习文件.docx','r')
# f.close()

# 2.w（只写）  如果文件存在，新建文件，执行写入，会覆盖原有的内容
# f = open('python练习文件.docx','w')
# f.write('缪泽平')
# f.close()

# 3.a （追加） ，如果文件不存在，新建文件。在原有的基础上，追加新内容
# f = open('python练习文件.docx','a')
# f.write(': 生命简短，我要python')
# f.close()

# 默认时：为（r）
# f = open('python练习文件.docx')
# f.close()

# 读写函数
# 1.read（）
# f = open('test.txt','a')
# f.write('cccccc')
# f = open('test.txt','r')
# print(f.read())

# 2.readlines（）读取所有行，并返还一个列表

# f = open('test.txt','r')    #为只读
# result = f.readlines()
# print(result)
# f.close()

# 3.readline    一次性只读取一行文件
# f = open('test.txt','r')
# print1 = f.readline()
# print(print1)
# print1 = f.readline()
# print(print1)
# print1 = f.readline()
# print(print1)
# f.close()
# i = 1

# c = 0
# f = open('test1.txt',"w")
# f.write('tom:10\nlily:12\njiele:11')
# f = open('test1.txt','r')
# while c <= 3:
#     i = f.readline()
#     print(i)
#     c += 1
# f.close()

# 二。访问模式特点二：
# 1.1 带 （+）的表示可读可写
# 1.2 带 （d）的都表示以二进制的格式操作文件
# 1.3 不管怎么变形都要遵循主访问模式的特点

# 2.r+ 没有文件时报错，文件指针在开头，所以能读取出来数据
# f = open('test.txt','r+')
# con = f.read()
# print(con)
# f.write('\naaa')
# a = f.tell()
# print(a)
# f.close()

# 3.w+ 没有文件时会新建文件：w的特点：文件指针在开头，用新内容覆盖原内容，（若没进行添加操作，这无法读取任何数据）
# i = open('test.txt1','w+')
# con = i.read()
# print(con)
# i.close()

# 4.a+ 没有文件时会新建文件，文件指针在结尾(所以什么数据也没有）
# a = open('test1.txt','a+')
# com = a.read()
# print(com)
# a.close()


# seek函数    语法： 文件对象.seek（偏移量，起始位置） 0开头 1当前位置 2结尾


# i = open('test1.txt','r+')
# # i.write('tom:10\nlily:12\njiele:11')
# print(i.tell())     #tell()用于查找文件指针的位置
# com = i.read()
# print(com)
# i.close()

# 1.在r即r+访问模式下改变文件指针的位置
# i = open('test1.txt','r+')
# # i.seek(6,0)   #从第6个字符开始读取
# i.seek(0,2)     #改变为从结尾进行访问
# com = i.read()
# print(com)
#
# i.close()

# 1.在a即a+访问模式下改变文件指针的位置
# i = open('test1.txt','a+')
# # # i.seek(0)     #一个0和两个0的效果是一样的。
# i.seek(0,0)
# com = i.read()
# print(com)
#
# # 三。文件备份
# 步骤：1.接受用户输入的文件名
#      2.规划备份文件的名字
#      3.备份文件写入数据（数据和原文件是一样的）

# 步骤1.
# old_name = input('请输入您要备份的文件：')
# # print(old_name)
# #
# # # 步骤2.
# mul = old_name.rfind('.')     #rfind()从后往前查找
# print(old_name[:mul])
# print(old_name[mul:])
# #
# if mul > 0:     #为了防止输入无效文件。
#     postfix = old_name[mul:]
#
# new_name = old_name[:mul] + '[备份]' + old_name[:mul]
# print(new_name)
# #
# # # 步骤3.
# # # 3.1打开备份文件和读取文件
# old_f = open(old_name,'r+')
# new_f = open(new_name,'w+')
# # # 3.2写入文件数据
# while True:
#     com = old_f.read(1024)   #运用循环来防止文件过大而导致电脑死机
#     if len(com) == 0:        #当长度为0时退出循环
#         break
#     new_f.write(com)
# # # 3.关闭文件
# old_f.close()
# new_f.close()



# 四。文件和文件夹的操作
'''
1.导入os模块
2使用模块内功能
'''
import os

# 1. rename(): 重命名文件
# os.rename('test.txt','test10.txt')

# 2. remove(): 删除文件
# os.remove('test1[备份].txt')

# 3. mkdir(): 创建文件夹
# os.mkdir('aa')

# 4. rmdir(): 删除文件夹
# os.rmdir('aa')

# 5. getcwd(): 返回当前文件所在目录的路径
# print(os.getcwd('C:\Users\wyys2\AppData\Flash Player'))

# 6.chdir(): 改变目录的路径
# os.mkdir('aa')  #先创建一个目录
# 需求：在aa里面创建bb的文件夹：1.切换目录到aa 2.创建bb
# os.chdir('aa')
# os.mkdir('bb')

# 7.listdir(): 获得某个文件夹下所有的文件，并返还一个列表
# print(os.listdir('D:\图片总集\动漫图片'))


# 8.rename()--重命名文件夹    bb重命名为bbbb
# os.chdir('bbbb')
# os.rename('bb','bbbb')


# 五。应用案例
# 批量文件重命名   (不要运行）

    # mul = len('python_')
    # new_name = i[mul:]
    # os.rename(i,new_name)














