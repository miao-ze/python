"""处理wed的框架（2）模块功能转换"""

import time

def not_fount():
    # 进行信息的封装
    # 1.状态信息
    status = "HTTP/1.1 404 Not Fount"
    # 2.响应头信息 注意：响应头信息一般有多个，所以信息要放在一个列表中，每项数据可以为，字典或元组
    respond_header = [("Server","MS miao")]
    # 3.响应体
    # wed处理后的数据
    # 获取当前时间
    respond_body = " 404 not found"

    """ 把处理后的结果返回给“处理动态资源请” 的函数，再让这个“处理动态资源请”函数返回给wed服务器  【这里返回的是元组】"""
    return status,respond_header,respond_body


# 当知道请求的是那个页面时：专门定义一个函数处理
def moban1():
    # 进行信息的封装
    # 状态信息
    status = "HTTP/1.1 200 OK"
    # 响应头信息 注意：响应头信息一般有多个，所以信息要放在一个列表中，每项数据可以为，字典或元组
    respond_header = [("Server","MS miao"),('Allow','GET,HEAD')]

    # 1.打开指定模块文件，读取文件中的数据
    with open("mini-wed素材/moban1.html", "r",encoding="utf-8") as file:
        file_date = file.read()

    # 2.查询数据库，模块里面的模块变量（{%comment%}） 替换完成后从数据库中查询数据
    '''在03中进行数据库查询数据，所以现在暂时替换成时间信息'''
    # 查询当前时间，模拟数据库内容
    times = time.ctime()
    respond_body = file_date.replace("{/%comment/%}",times)

    return status,respond_header,respond_body

# 处理动态资源请求
def handler(env): # 传入导入的信息
    # 由于传入的是一个字典信息
    requests_path = env['requests_path']
    print("传入的请求路径信息是：",requests_path)

    '''获取具体请求的页面'''
    # 如果请求地址是（moban1）这获取模板的信息，（信息在新建的函数中）
    if requests_path == "/moban1.html":
        # 获取首页数据
        result = moban1()
        #把处理后的结果返回给wed服务器，让wed服务器拼接响应报文是使用
        return result

    # 设置放回404的信息
    else:
        result = not_fount()
        return result

