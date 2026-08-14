import socket
import threading
import sys
'''
明确思路：
1.以面向对象的方法进行开发要想象出Wed服务器的属性和方法
2.wed服务器都要有的是socket属性，方法可以定义成进行工作--->接受用户信息在返还资料
'''


class WedHttpServer(object):
    #定义初始的属性 有socket套接字
    def __init__(self,port):
        # 创建服务端的socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # *设置端口号复用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 对服务器绑定ip和端口号
        server_socket.bind(("", port))
        # 设置监听
        server_socket.listen(128)
        '''把wed的socket作为工作的属性'''
        self.server_socket = server_socket


    '''创建子线程'''
    @staticmethod       #设置静态方法
    def client_server(new_socket):
        print('用户编号已进入')
        # 用户的回复
        respond1 = new_socket.recv(4096)
        respond2 = respond1.decode('utf-8')
        if len(respond2) == 0:
            new_socket.close()
            print(f'已断开客户的连接')
            return
        respond1_path = respond2.split(' ', maxsplit=2)
        respond1_true = respond1_path[1]
        '''当用户访问的是主页时'''
        if respond1_true == '/':
            with open("C:\\python网络爬虫视频\\python高级\\05 web服务器\\3 web服务器\\文件\\wenjian.html",
                      'rb') as file:
                file_data = file.read()
            # 1.响应行
            respond_hang = 'HTTP/1.1 200 OK\r\n'  # "\r\n"很重要
            # 2.响应头
            respond_header = 'Server: PWS/1.0\r\n'
            # 3.空行
            # 4.响应体（源代码）
            respond_body = file_data
            # 进行封装
            respond_data = (respond_hang + respond_header + '\r\n').encode('utf-8') + respond_body
            # 进行发送给用户端浏览器
            new_socket.send(respond_data)
            new_socket.close()
            return
        else:
            try:
                '''设置响应体'''
                with open(f"C:\\python网络爬虫视频\\python高级\\05 web服务器\\3 web服务器\\文件\\{respond1_true}",
                          'rb') as file:
                    file_data = file.read()

                '''当访问的页面不存在时个用户返还404数据的页面'''
            except Exception as e:
                with open("C:\\python网络爬虫视频\\python高级\\05 web服务器\\3 web服务器\\文件\\error.html",
                          'rb') as file:
                    file_data = file.read()
                # 设置返回用户固定的页面（要进行设置返回浏览器的响应头，要进行封装）
                # 1.响应行
                respond_hang = 'HTTP/1.1 404 NOT FOUNT\r\n'  # 设置404页面的响应行
                # 2.响应头
                respond_header = 'Server: PWS/1.0\r\n'
                # 3.空行
                respond_kong = "\r\n"
                # 4.响应体（源代码）
                respond_body = file_data
                # 进行封装
                respond_data = (respond_hang + respond_header + '\r\n').encode('utf-8') + respond_body
                # 进行发送给用户端浏览器
                new_socket.send(respond_data)
                '''当页面存在时执行返还指定的页面'''
            else:
                # 设置返回用户固定的页面（要进行设置返回浏览器的响应头，要进行封装）
                # 1.响应行
                respond_hang = 'HTTP/1.1 200 OK\r\n'  # "\r\n"很重要
                # 2.响应头
                respond_header = 'Server: PWS/1.0\r\n'
                # 3.空行
                respond_kong = "\r\n"
                # 4.响应体（源代码）
                respond_body = file_data
                # 进行封装
                respond_data = (respond_hang + respond_header + '\r\n').encode('utf-8') + respond_body
                # 进行发送给用户端浏览器
                new_socket.send(respond_data)
                '''最后不管存不存在都要关闭页面'''
            finally:
                # 关闭给用户的socket
                new_socket.close()


        #定义方法即：进行工作 就是启动服务器的方法 --->(注意：这里是主方法就是主线程)
    def work(self):
        while True:
            new_socket, ip_port = self.server_socket.accept()
            print('新用户：', ip_port)
            #明确：主线程的任务以接受完用户了，现在要开辟子线程，来返回页面
            new_client = threading.Thread(target=self.client_server, args=(new_socket,), daemon=True)
            # 设置守护主线程
            # 启动主线程
            new_client.start()


'''用类创建对象'''
def main():
    #获得命令行参数
    pamrms = sys.argv
    #对获得到的参数进行判断
    #1.判断参数的数量是否正确
    if len(pamrms) != 2:
        print('输入的格式错误！数量错')
        return
    #2.判断第二个参数是不是由数字组成的
    if not pamrms[1].isdigit():     #isdigit用来判断字符串是否由数字组成的
        print('输入的格式错误！类型错')
        return
    # 代码进行到次得到的参数是正确的
    port = int(pamrms[1])
    wed_server = WedHttpServer(port)
    wed_server.work()

if __name__ == '__main__':
    main()