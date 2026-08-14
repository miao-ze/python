# 1.异常的写法
'''
try:
    可能发生错误的代码
except:
    如果出现异常时执行的代码
'''
# 快速体验
# try:
#     flie1 = open('test.txt','r')
# except:
#     flie1 = open('test.txt','w')

#2.捕获指定异常
# 语法
'''
try:
    可能发生错误的代码
except 异常类型 as xx:
    如果捕获到该异常类型时执行的代码   


注意：如果尝试执行的代码的异常类型与要捕获的异常类型不一致时，则无法捕获异常
'''

# try:
#     print(mul)
# except NameError:
#     print('有问题')


#2.捕获多个指定异常
#当无法确定是什么异常是用
# try:
#     print(1/0)
# except (NameError,ZeroDivisionError):   #(以元组接收)
#     print('有异常')


# 2.1 捕获异常描述信息

# try:
#     flie1 = open('test.txt','r')
# except (NameError,FileNotFoundError) as result:  #把捕获的异常信息储存在as后的变量中，在打印这个变量
#     print(result)

# 3.捕获所有异常
#关键子：Exception
# try:
#     print(mul)
# except Exception as flie1:
#     print(flie1)


# 4.异常的else
# else表示的是没有异常时要执行的代码
# try:
#     print(1)
# except Exception as flie2:
#     print(flie2)
# else:
#     print('没有错误')
#
#

# 5.异常的finally
# finally表示的时无论是否异常都要执行的代码 如：（关闭文件）
# try:
#     f = open('1.txt','r')
# except Exception as result:
#     print(result)
#     f = open('1.txt',"w")
# else:
#     print('没问题') #因为有异常所以没有执行
# finally:
#     f.close()


# 三。异常地传递(嵌套书写)
'''拓张在命令提示符中运行'''
#1.尝试以只读打开文件，如文件存在则读取内容，不存在则提示用户
#2.循环读取内容，当无内容是退出循环，若用户意外终止，则提示用户意外终止

# import time
# try:
#     f = open('客户信息.txt',encoding='utf-8')
#     try:
#         while True:
#             line = f.readline()
#             if not line:    #当没有更多行可读时，line 会是空字符串
#                 break
#             time.sleep(3)
#             print(line)
#     except:
#         #在命令提示符中如果按下：ctrl+c结束终止的键
#         print('程序异常终止了')
# except Exception:
#     print('该文件不存在')

# 四。自定义异常
# 在python中，抛出自定义异常的语句为raise异常类对象
# 需求：密码长度不足，则报异常（用户输入密码，如果输入的密码的长度不足三位，则报错，即抛出自定义异常，并捕获该异常）

'''自定义异常类，继承Exception'''
# class WoDeError(Exception):
#     def __init__(self,length,mim_length):
#         self.length = length
#         self.min_length = mim_length
#     def __str__(self):      #设置异常描述信息（用魔法方法）
#         return f'您输入的密码的长度是{self.length},密码长度不少于{self.min_length}'
"""抛出异常： raise 异常类名()"""
# def main():
#     try:
#         phone = input('请输入密码: ')
#         if len(phone) < 3:
#             #抛出异常类创建的对象
#             raise WoDeError(len(phone),3)
#     except WoDeError as result:       #捕获异常
#         print(result)
#     else:
#         print('密码格式正确')
#
#
# main()
#


# while True:
#     try:
#         name = input('请输入您的名字：')
#         socore = input('请输入您的电话号码：')
#         if len(socore) != 11:
#             raise Exception('您输入的位数异常')
#         if not socore.isdigit():
#             raise Exception('必须为数字')
#         with open('分数成绩表.txt','a+',encoding='utf-8') as file:
#             file.write(name+'\t'+socore+'\n')
#     except Exception as reasult:
#         print(reasult)





#断言assert
while True:
    def fenshu(i):
        try:
            assert i >= 0 and i <= 100,"您的分数必须在0~100之间"
            if i >= 90:
                return '优秀'
            if i >= 80:
                return '良好'
            if i >= 70:
                return '良好'
            if i >= 60:
                return '及格'
            else:
                return '不及格'
        except AssertionError as e:
            print(e)
            return None
        except Exception as e:
            print(e)


socore = int(input('请输入您的分数：'))
fenshu(socore)









