# 1.导包
import pymysql
if __name__ == '__main__':
    # 2.创建连接对象 connect = Connect = Connection 使用这三个里面中的任意一个函数都可以创建连接
    conn = pymysql.connect(host="localhost",
                    port=3306,
                    user='root',
                    password='1901420817',
                    database='python1',
                    charset='utf8')
    # 3.获取游标，目的就是要执行sql语句 ---> cursor()
    cursor = conn.cursor()
    while True:
        # 准备sql，之前在MySQL客户端如何编写sql，在python程序还怎么编写
        sql = input("输入sql语句命令（要退出请输入结束）：")
        if sql != '结束':
            try:
                # 4.执行SQL语句
                # 准备完后，开始执行 execute(sql) 注意：用创建的游标来执行
                cursor.execute(sql)
                # 进行数据的提交 注意：用创建链接的对象进行提交，而非用游标
                conn.commit()
            except Exception as e:
                print('语法错误！')
                continue

            else:
                # 获取查询的结果
                result2 = cursor.fetchall()
                for i in result2:
                    print(i)
                continue
        else:
            # 5.关闭游标
            cursor.close()
            # 6.关闭连接
            conn.close()
            print('已结束')
'''对数据库中的数据进行了增删该操作后要用 commit进行提交，也可用rollback进行回滚撤销'''