import socket
import threading
# 导入自己创建的wed框架
# import wed_framework1
'''wed_framework2 模块功能转换'''
# import wed_framework2
'''wed_framework3 创建路由列表'''
import wed_framework3
'''wed_framework4 用装饰器进行路由列表的自动添加'''
# import wed_framework4
'''wed_framework5 连接MySQL数据库进行数据的拼接'''
import wed_framework5
"""wed_framework6 json学生信息数据接口的开发"""
# import wed_framework6
"""wed_framework7 用html模块中的ajax返送请求"""
import wed_framework7

'''
明确思路：
1.以面向对象的方法进行开发要想象出Wed服务器的属性和方法
2.wed服务器都要有的是socket属性，方法可以定义成进行工作--->接受用户信息在返还资料
'''


class WedHttpServer(object):
    #定义初始的属性 有socket套接字
    def __init__(self):
        # 创建服务端的socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # *设置端口号复用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 对服务器绑定ip和端口号
        server_socket.bind(("", 9000))
        # 设置监听
        server_socket.listen(128)
        '''把wed的socket作为公共的属性'''
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
            with open("mini-wed素材\\zhuye.html",
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




        """设置动态请求"""
        if respond1_true.endswith(".html"):
            # 动态请求找wed框架进行处理，所以需要把请求参数给wed框架
            # 准备给wed框架的参数信息,参数信息都要放在字典中
            env = {
                "requests_path":respond1_true,
                # 传入请求头信息
            }
            # 使用自己创建的wed框架，并导入信息
            # 1.wed框架需要把处理结果返回wed服务器
            # 2.wed服务器需要负责把返回的结果封装成相应报文送给浏览器
            """（一）：获取框架处理的结果"""
            status,respond_header,respond_body = wed_framework7.handler(env)
            # 获取完信息后拼装成http响应报文
            # 1.响应行
            respond_line = status + "\r\n"
            # 2.响应头
            respond_headers = ""
            '''由于返回的是列表所以要进行遍历'''
            for i in respond_header:
                # 注意格式：1。冒号后以一个空格，2。每条响应头数据后都要加上空行（\r\n）
                respond_headers += "%s: %s\r\n" % i
            # 3.空行
            # 4.响应体
            respond_body = respond_body
            #进行拼接
            responds = respond_line + respond_headers + "\r\n" + respond_body
            #进行发送
            new_socket.send(responds.encode('utf-8'))
            #关闭链接
            new_socket.close()



        # 设置静态请求
        else:
            try:
                with open(f"html文件\\{respond1_true}",
                            'rb') as file:
                    file_data = file.read()

                '''当访问的页面不存在时个用户返还404数据的页面'''
            except Exception as e:
                with open("html文件\\error.html",
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
            # daemon = True 表示设置守护主线程
            # 启动主线程
            new_client.start()




'''用类创建对象'''
def main():
    wed_server = WedHttpServer()
    wed_server.work()

if __name__ == '__main__':
    main()