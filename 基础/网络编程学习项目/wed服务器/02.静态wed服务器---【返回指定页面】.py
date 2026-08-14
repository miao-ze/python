import os




def main():
    with open(f"C:\\python网络爬虫视频\\python高级\\05 web服务器\\3 web服务器\\文件\\p.html", 'rb') as file:
        file_data_usually = file.read()
    #创建服务端的socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # *设置端口号复用
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #对服务器绑定ip和端口号   http://localhost:9000/p.html
    server_socket.bind(("",9000))
    #设置监听
    server_socket.listen(128)
    while True:
    #设置等待用户
        new_socket,ip_port = server_socket.accept()
        print('用户编号：',ip_port,'已进入')
        #用户的回复
        respond1 = new_socket.recv(4096)
        respond2 = respond1.decode('utf-8')
        if len(respond2) == 0:
            new_socket.close()
            print(f'已断开客户：{ip_port} 的连接')
            continue
        respond1_path = respond2.split(' ',maxsplit=2)
        respond1_true = respond1_path[1]
        if respond1_true == '/':
            file_data = file_data_usually
        else:
            '''设置响应体'''
            with open(f"C:\\python网络爬虫视频\\python高级\\05 web服务器\\3 web服务器\\文件\\{respond1_true}",'rb') as file:
                file_data = file.read()
        #设置返回用户固定的页面（要进行设置返回浏览器的响应头，要进行封装）
        # 1.响应行
        respond_hang = 'HTTP/1.1 200 OK\r\n'   #"\r\n"很重要
        # 2.响应头
        respond_header = 'Server: PWS/1.0\r\n'
        # 3.空行
        respond_kong = "\r\n"
        # 4.响应体（源代码）
        respond_body = file_data
        #进行封装
        respond_data = (respond_hang + respond_header + '\r\n').encode('utf-8') + respond_body
        #进行发送给用户端浏览器
        new_socket.send(respond_data)
        #关闭给用户的socket
        new_socket.close()

import socket
if __name__ == '__main__':
    main()
