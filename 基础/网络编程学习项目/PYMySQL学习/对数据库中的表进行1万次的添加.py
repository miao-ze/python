
import pymysql

if __name__ == '__main__':

    coon = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1901420817',
                           database='python1',
                           charset='utf8')

    cursor = coon.cursor()

    sql = "insert into test_index(name) values(%s);"
    try:
        for i in range(10000):
            cursor.execute(sql,["text" + str(i)])
        coon.commit()
    except Exception as e:
        print('sql语法错误！')
        coon.rollback()
    finally:
        cursor.close()
        coon.close()
