import socket
import threading
import framework_complete_end
import logging

# 设置日志等级
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[lineno:%(lineno)id]-%(levelname)s-%(message)s',
                    filename='logging.txt',
                    filemode='a',
                    encoding="utf-8")

class WedServer(object):
    def __init__(self):
        # 配置服务器的套接字（socket）
        socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 绑定端口号
        socket_server.bind(("",8000))
        # 配置端口号释放
        socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        # 设置监听
        socket_server.listen(128)
        # 将套接字（socket）实例化
        self.socket_server = socket_server


    # 设置静态方法，这样就可以传入新的套接字了（new_socket）
    @ staticmethod
    # 设置子线程
    def work_server(new_socket,ip_port):
        print(f"用户{ip_port}已进入")
        # 得到用户发出的请求信息
        client_request = new_socket.recv(1024)
        # 先对信息进行编码为utf-8 的形式，因为发来的数据是bytes类型
        client_request_decode = client_request.decode('utf-8')

        '''判断1：当用户断开连接时'''
        if len(client_request_decode) == 0:
            print("用户已经断开连接")
            new_socket.close()
            return
        # 此信息是以http格式形式发送的，需要对其进行分解得到其请求路径信息
        request_split = client_request_decode.split(' ',maxsplit=2)
        # 接下来取到用户请求的网址地址，由于requests请求报文，是以请求行、请求头、空行、发送到wed服务器的
        # 所以我们需要请求行中的第二项信息，即请求路径
        request_rout = request_split[1]
        print("请求路径是：",request_rout)
        # 现在已经知道了用户的具体请求路径，所以要进行资源的返回：以http相应报文的形式返回

        '''判断2；当路径是主目录资源地址时'''
        if request_rout == "/":
            # 1.设置响应行 注意写结束换行符”\r\n“
            respond_line = "HTTP/1.1 200 OK\r\n"
            # 2.设置响应头 注意写结束换行符”\r\n“
            respond_header = "Server: MS.miao\r\nConnection: keep-alive\r\n"
            # 3.空行 之后在拼接相应报文时一并添加
            # 4.响应体
            with open('mini-wed素材\\zhuye.html','r',encoding='utf-8') as file:
                file_date = file.read()
            respond_body = file_date
            # 进行相应报文的拼接 【注意：要转成bytes类型发送给浏览器】
            respond_message = (respond_line + respond_header + "\r\n"+ respond_body).encode('utf-8')
            # 发送响应报文
            new_socket.send(respond_message)
            # 关闭套接字（new_socket）
            new_socket.close()
            return


        '''判断3：当请求路径是动态页面请求时'''
        # 用endswith方法进行判断
        if request_rout.endswith(".html"):
            '''动态资源请求:设置日志'''
            logging.info('动态资源请求：' + request_rout)
            # 进行到此已经可以确定，是动态页面请求了，所以此时wed服务器要请求wed框架
            # wed框架需要返还模板文件，包括相应行信息、响应头信息、响应体信息，
            respond_line,respond_header,respond_body = framework_complete_end.work_choose(request_rout)
            # 对返还的数据进行拼接
            # 1.制作响应行
            respond_lines = respond_line + '\r\n'
            # 2.制作响应头 【注意在wed框架中响应头是列表，列表中包含以元组为元素的各个数据】
            # 准备空响应头，进行拼接
            respond_headers = ''
            for value in respond_header:
                respond_headers += "%s: %s\r\n" % value
            # 3.准备空行
            # 4.制作响应体
            respond_body_s = respond_body
            # 进行拼接 【并编码成bytes类型】
            responds_all = (respond_lines + respond_headers + "\r\n" + str(respond_body_s) ).encode('utf-8')
            print(responds_all)
            # 进行发送
            new_socket.send(responds_all)
            # 关闭连接
            new_socket.close()
            return


    def work(self):
        # 设置循环来，接受不同的用户
        while True:
            # 设置主线程：用来等待接受用户,把具体的服务工作给子线程去做
            # 接受到用户时，会返回新的套接字（socket），和用户的id
            new_socket,ip_port = self.socket_server.accept()
            # 设置子线程，并让其守护主线程 【注意：在指明子线程方法时，要加self】
            work_thread_server = threading.Thread(target=self.work_server,args=(new_socket,ip_port),daemon=True)
            # 启动子线程
            work_thread_server.start()


def work_server_start():
    wed_server_complete = WedServer()
    wed_server_complete.work()


if __name__ == '__main__':
    work_server_start()