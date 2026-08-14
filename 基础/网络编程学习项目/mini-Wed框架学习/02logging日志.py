
# 先导入logging包
import logging

'''
logging日志有五个级别
1.debug 在程序调式时使用，所以上线后不适用次级别
2.info  程序正常运行时使用
3.warning 程序未按预期运行，但并非错误，而是不如说：用户在登录时密码输入错误
4.error  程序错误时使用
5.critical 表示特别严重的错误
'''

# 设置日志等级 --> 用logging.basicConfig()
logging.basicConfig(level=logging.DEBUG,
                    #可通过format设置输出格式
                    # 1.%(asctime)s                     当前时间
                    # 2.%(filename)s[line:%(lineno)d]   文件名和行号
                    # 2.%(levelname)s                   日志级别
                    # 4.%(filename)s                    日志信息
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(filename)s',
                    #可通过filename来把日志信息写到文件中
                    filename="logging.txt",filemode="a",
                    #设置写入使用的编码格式
                    encoding="utf-8")

# 输出不同级别的日志
logging.debug("我是一个debug级别的日志")
logging.info("我是一个info级别的日志")
logging.warning("我是一个warning级别的日志")
logging.error("我是一个error级别的日志")
logging.critical("我是一个critical级别的日志")

'''注意：默认情况是warning级别，所以只有大于等于warning级别才会显示'''

