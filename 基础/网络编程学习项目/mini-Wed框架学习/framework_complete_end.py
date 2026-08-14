import pymysql
import json
import logging


# 准备路由列表，
rout_list = []

''' 准备步骤：定义带参数的修饰器来自动添加路由'''
def rout(request_rout):

    def decorate(func):
        rout_list.append((request_rout,func))
        def inner():
            result = func()
            return result
        return inner

    return decorate


'''1.定义返回404页面的静态文件'''
def error():
    # 1.设置相应行
    respond_line = "HTTP/1.1 404 Not Fount"
    # 2.设置响应头
    respond_header = [("Server","MS.miao"),("Connection","keep-alive")]
    # 3.设置响应体
    with open("mini-wed素材/error.html",'r',encoding='utf-8') as file:
        file_date = file.read()
    respond_body = file_date
    # 返还数据到wed服务器中，再由wed服务器进行数据的拼接 【但在这里是在执行修饰器中的函数】
    return respond_line,respond_header,respond_body



'''2.定义用来处理静态数据的函数'''
@ rout('/moban1.html')  # ---> request_rout == "/moban1.html" ; decorate(moban1) ----> func == "moban1"
def moban1():
    # 1.设置相应行
    respond_line = "HTTP/1.1 200 OK"
    # 2.设置响应头
    respond_header = [("Server","MS.miao"),("Connection","keep-alive")]
    # 3.设置响应体
    with open("mini-wed素材/moban1.html",'r',encoding='utf-8') as file:
        file_date = file.read()
    respond_body = file_date
    # 返还数据到wed服务器中，再由wed服务器进行数据的拼接 【但在这里是在执行修饰器中的函数】
    return respond_line,respond_header,respond_body



'''3.定义要从数据库中取出数据，并拼接到html代码中的动态文件'''
@ rout("/moban2.html")
def moban2():
    # 1.设置相应行
    respond_line = "HTTP/1.1 200 OK"
    # 2.设置响应头
    respond_header = [("Server", "MS.miao"), ("Connection", "keep-alive")]
    # 3.读取数据库中的数据
    conn = pymysql.connect( host='localhost',
                            port=3306,
                            user='root',
                            password='1901420817',
                            database='mokuai1',
                            charset='utf8')
    cursor = conn.cursor()
    sql = "select * from students2;"
    cursor.execute(sql)
    # 得到数据库中需要的数据
    mysql_date = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 4.得到模板文件
    with open('mini-wed素材/moban2.html',"r",encoding='utf-8') as file:
        file_date = file.read()
    # 5.将数据库中的数据拼接到模板文件中 【用replace替代方法】
    # 进行封装html中要进行拼装并要添加的数据
    respond_body = ''
    for value in mysql_date:
        # 注意标签的缩进要与原html中要提替代位置的缩进相同
        respond_body += f'''
            <tr>
                <td>{value[0]}</td>
                <td>{value[1]}</td>
                <td>{value[2]}</td>
                <td>{value[3]}</td>
                <td>{value[4]}</td>
                <td>{value[5]}</td>
                <td>{value[6]}</td>
            </tr>   
                        '''
    respond_body_s = file_date.replace("{/%comment%/}",respond_body)

    print('数据库中的数据为：',mysql_date)
    list_dict = []
    for i in mysql_date:
        list_dict.append({"id":i[0],"number":i[1],"name":i[2],"sex":i[3],"class":i[4],"height":i[5],"age":i[6]})
    print()
    print()
    print()
    print()
    # print("改进后：",list_dict)
    json_date = json.dumps(list_dict,ensure_ascii=False)
    print(json_date)
    print(type(json_date))
    # 6.返还所有数据到wed服务器
    return respond_line,respond_header,respond_body_s


'''4.定义得到json数据的函数，为发送ajax请求提供数据支撑：json数据来源于数据库'''
@ rout("/moban3_json_date.html")
def moban3_json_date():
    # 1.设置相应行
    respond_line = "HTTP/1.1 200 OK"
    # 2.设置响应头 【注意这里要指定浏览器的编码格式，因为是单独发送的，没有模板文件。这样json数据就可以解读】
    respond_header = [("Server", "MS.miao"), ("Connection", "keep-alive"),
                      ("Content-Type","text/html;charset=utf-8")]
    # 3.读取数据库中的数据
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1901420817',
                           database='mokuai1',
                           charset='utf8')
    cursor = conn.cursor()
    sql = ("select s.id,s.code,s.name,s.sex,s.class_name,s.height,s.age,m.message "
           "from students2 s inner join messages2 m on"
           " s.code = m.studend_code;")
    cursor.execute(sql)
    # 得到数据库中需要的数据
    mysql_date = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print(mysql_date)
    # 4.将从mysql数据库中得到元组数据转换成json数据：(这里分为了两个步骤)
    # 4.1.步骤一，将这个元组嵌套转成列表字典               可以用列表推导式进行转换
    json_date1 = [{"id":data[0],
                 'code':data[1],
                 'name':data[2],
                  'sex':data[3],
                  'class_name':data[4],
                  'height':data[5],
                  'age':data[6],
                  'message':data[7]} for data in mysql_date]

    print("转换前：", type(json_date1))
    # 4.2 步骤二：用json.dumps()将列表字典转成json数据形式
    # ensure_ascii=False 的作用是可以显示中文
    json_date2 = json.dumps(json_date1,ensure_ascii=False)
    print("转换后：",type(json_date2))
    # 5. 现在可以将json数据发送给浏览器
    respond_body = json_date2
    return respond_line,respond_header,respond_body



'''5.通过ajax请求，得到json数据，并把json数据绑定到模板文件中相应的位置'''
'''注意这里的数据传递方式有所不同：
   这里是先把模板文件发送给浏览器，再由模板文件中的jquery代码，发送ajax请求。
   得到json数据，把json数据解析后，在进行拼接到相应的位置
   '''
@ rout("/moban3.html")
def moban3():
    # 1.设置相应行
    respond_line = "HTTP/1.1 200 OK"
    # 2.设置响应头 【注意这里要指定浏览器的编码格式，因为是单独发送的，没有模板文件。这样json数据就可以解读】
    respond_header = [("Server", "MS.miao"), ("Connection", "keep-alive"),
                      ("Content-Type", "text/html;charset=utf-8")]
    # 3.查询模板文件
    with open("mini-wed素材/moban3_1.html",'r',encoding='utf-8') as file:
        file_date = file.read()
    respond_body = file_date
    # 4.返回数据到wed服务器
    return respond_line,respond_header,respond_body


'''# 附加'''
@ rout("/jquery_study.html")
def jquery_study():
    # 1.设置相应行
    respond_line = "HTTP/1.1 200 OK"
    # 2.设置响应头 【注意这里要指定浏览器的编码格式，因为是单独发送的，没有模板文件。这样json数据就可以解读】
    respond_header = [("Server", "MS.miao"), ("Connection", "keep-alive"),
                      ("Content-Type", "text/html;charset=utf-8")]
    # 3.查询模板文件
    with open("mini-wed素材/jquery_study.html",'r',encoding='utf-8') as file:
        file_date = file.read()
    respond_body = file_date
    # 4.返回数据到wed服务器
    return respond_line,respond_header,respond_body

@ rout('/json_study.html')
def json_study():
    # 1.设置相应行
    respond_line = "HTTP/1.1 200 OK"
    # 2.设置响应头 【注意这里要指定浏览器的编码格式，因为是单独发送的，没有模板文件。这样json数据就可以解读】
    respond_header = [("Server", "MS.miao"), ("Connection", "keep-alive"),
                      ("Content-Type", "text/html;charset=utf-8")]
    respond_body = json.dumps({'姓名':'小红','年龄':'18'})

    return respond_line, respond_header, respond_body


def work_choose(sql):
    # 显示用户动态请求的资源地址
    print("用户的动态请求路径是：",sql)
    # 接下来需要根据路径执行相应的函数
    # 这里用路由的方式进行选择相应的函数进行执行
    for request_rout,func in rout_list:
        if sql == request_rout:
            result = func()
            return result
    else:
        result = error()
        logging.error('没有设置相关的路由信息：' + sql)
        return result

if __name__ == '__main__':

    print(rout_list)