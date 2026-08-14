# 1.导包
import pymysql
if __name__ == '__main__':
    # 2.创建连接对象 connect = Connect = Connection 使用这三个里面中的任意一个函数都可以创建连接
    '''
    1.host: 服务器的主机地址
    2.port：mysql数据库的端口号
    3.user；用户名
    4.password；密码
    5.database；所要进行操作的数据库
    6.charset；操作数据库所使用的编码格式
    '''
    conn = pymysql.connect(host="localhost",
                    port=3306,
                    user='root',
                    password='1901420817',
                    database='python1',
                    charset='utf8')
    # 3.获取游标，目的就是要执行sql语句 ---> cursor()
    cursor = conn.cursor()
    # 准备sql，之前在MySQL客户端如何编写sql，在python程序还怎么编写
    sql = "select * from student1;"
    # 4.执行SQL语句
    # 准备完后，开始执行 execute(sql) 注意：用创建的游标来执行
    cursor.execute(sql)

    # 获取查询的结果
    # * fetchone() : 获取一条结果
    result1 = cursor.fetchone()
    # print(result1)
    # * fetchall() : 获取多个结果(就跟在客户端一样)
    result2 = cursor.fetchall()
    # print(result2)
    for i in result2:
        print(i , end=" ")
    # 5.关闭游标
    cursor.close()
    # 6.关闭连接
    conn.close()