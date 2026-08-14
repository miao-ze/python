""" wed框架 --【构建学生信息数据接口】"""
import pymysql
import time
import json

# 定义路由列表
route_list = []
# 定义一个带有参数的装饰器的函数，作用是：自动添加路由列表
def rount(path):
    # 定义装饰器
    def decorate(func):
        # 进行路由的添加 : 当执行装饰器时就把路由列表进行添加
        route_list.append((path,func))

        def inner(func):
            # 切记不要在被执行时在添加，不然会导致重复添加
            result = func()
            return result
        return inner
    return decorate


# 当页面不存在时返回的数据
def not_fount():
    # 进行信息的封装
    # 1.状态信息
    status = "HTTP/1.1 404 Not Fount"
    # 2.响应头信息 注意：响应头信息一般有多个，所以信息要放在一个列表中，每项数据可以为，字典或元组
    respond_header = [("Server","MS miao")]
    # 3.响应体
    respond_body = " 404 not found"
    """ 把处理后的结果返回给“处理动态资源请” 的函数，再让这个“处理动态资源请”函数返回给wed服务器  【这里返回的是元组】"""
    return status,respond_header,respond_body


"""1.不进行数据的替换"""
@ rount("/jquery_study.html")
# 当知道请求的是那个页面时：专门定义一个函数处理
def ajaxstudy():
    # 进行信息的封装
    # 状态信息
    status = "HTTP/1.1 200 OK"
    # 响应头信息 注意：响应头信息一般有多个，所以信息要放在一个列表中，每项数据可以为，字典或元组
    respond_header = [("Server","MS miao"),('Allow','GET,HEAD')]
    # 1.打开指定模块文件，读取文件中的数据
    with open("mini-wed素材/jquery_study.html", "r", encoding="utf-8") as file:
        file_date = file.read()
    respond_body = file_date
    #返回 响应行，响应头，响应体信息给wed服务器，再让wed服务器进行拼接，返回给浏览器
    return status,respond_header,respond_body

"""2.先把数据替换成时间"""
@ rount('/moban1.html')  #---> @decorate -->moban1 = decorate(moban1)
# 当知道请求的是那个页面时：专门定义一个函数处理
def moban1():
    # 进行信息的封装
    # 状态信息
    status = "HTTP/1.1 200 OK"
    # 响应头信息 注意：响应头信息一般有多个，所以信息要放在一个列表中，每项数据可以为，字典或元组
    respond_header = [("Server","MS miao")]
    # 1.打开指定模块文件，读取文件中的数据
    with open("mini-wed素材/moban1.html", "r",encoding="utf-8") as file:
        file_date = file.read()
    # 2.查询数据库，模块里面的模块变量（{%comment%}） 替换完成后从数据库中查询数据
    '''在下一个模板中进行数据的查询，所以现在暂时替换成时间信息'''
    # 查询当前时间，模拟数据库内容
    times = time.ctime()
    respond_body = file_date.replace("{/%comment/%}",times)
    return status,respond_header,respond_body



"""3.把数据替换成数据库中的数据，进行替换到html中"""
@ rount("/moban2.html")
def moban2():
    status = "HTTP/1.1 200 OK"
    respond_header = [("Server","MS miao"),("Host","http://www.miao.com/")]
    # 1.读取模板html
    with open("mini-wed素材/moban2.html",'r',encoding='utf-8') as file:
        file_date = file.read()
    # 2.读取mysql数据库中的数据
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password='1901420817',
                           database="mokuai1",
                           charset='utf8')
    cursor = conn.cursor()
    sql = "select * from students2"
    cursor.execute(sql)
    # 得到数据库中的数据
    sql_date = cursor.fetchall()
    cursor.close()
    conn.close()
    # 3.进行数据的拼接
    # 准备数据的变量
    dates = ""
    # 对每条数据进行遍历
    for values in sql_date:
        dates += """
                <tr>
                <td style="padding-top: 10px;">%s</td>
                <td>%s</td>
                <td >%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>   
                </tr>
                """ % values
    respond_body = file_date.replace("{/%comment%/}",dates)
    return status,respond_header,respond_body


"""4.返回json数据给浏览器"""
'''绑定url'''
@ rount("/center_date.html")
#学生信息中心数据接口
def center_date():
    # 1.从数据库中查询到数据，然后把查询到的数据转成json数据
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password='1901420817',
                           database="mokuai1",
                           charset='utf8')
    cursor = conn.cursor()
    sql = ("select s.id,s.code,s.name,s.sex,s.class_name,s.height,s.age,m.message "
           "from students2 s inner join messages2 m on"
           " s.code = m.studend_code;")
    cursor.execute(sql)
    # 得到数据库中的数据
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    '''进行数据格式的转换 元组--->转成json数据'''
    # 1.第一步：把元组转成列表字典 用列表推导式
    center_date_list = [ {"id":row[0],
                          "code":row[1],
                          "name":row[2],
                          "sex":row[3],
                          "class_name":row[4],
                          "height":row[5],
                          "age":row[6],
                          "message":row[7]} for row in result]
    #2.第二部：把列表转成接送字符串数据 用json.dupms()进行转换
    # 【由于转成json数据时，汉字会自动进行编码，要想显示参数要加一个参数，使其不由asc码进行编辑】
    # 参数ensure_ascii=False 表示在控制台中能狗显示中文
    json_str = json.dumps(center_date_list,ensure_ascii=False)
    #要把信息返回给wed，设置响应报文
    status = "HTTP/1.1 200 OK"
    '''设置响应头，指定浏览器的编码方式'''
    respond_header = [("Server", "MS miao"), ("Host", "http://www.miao.com/"),
                      # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
                      ("Content-Type","text/html;charset=utf-8")]
    return status,respond_header,json_str





"""0.导入wed服务器中要进行动态请求的路径，并执行相应的函数"""
# 处理动态资源请求
def handler(env): # 传入导入的信息
    # 由于传入的是一个字典信息
    requests_path = env['requests_path']
    print("传入的请求路径信息是：",requests_path)
    # 进行遍历寻找对应要执行的函数(之后要进行函数的执行添加只要在路由列表中进行添加即可)
    for path,func in route_list:
        if path == requests_path:
            result = func()
            return result
    else:
        result = not_fount()
        return result


if __name__ == '__main__':
    print(route_list)


