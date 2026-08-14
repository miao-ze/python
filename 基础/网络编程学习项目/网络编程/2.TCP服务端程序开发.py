import socket


if __name__ == '__main__':
    #1.创建服务端的socket
                 #               1.设置socket的ip的、类型为ipv4，2.设置socket的传输方式为TCP形式
    client_service = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2.为服务端的socket绑定ip和端口号
                        #以元组的形式传递IP、端口号（但一般第一个参数不指定，表示本机的任意ip）
    client_service.bind(("",9090))
    #3.设置监听
                        # 128 表示最大等待建立连接的个数为128个
    client_service.listen(128)
    #4.设置等待 -----> 等待接受客户端连接请求：使用accept方法，会阻塞代码，直到客户端到来，返回一个元组
    new_client,ip_port= client_service.accept() #返回的元组，包含新的socket和客户端的ip和端口号
    print('客户端IP和端口号为：',ip_port)
    #代码执行到此，说明客户端和服务端建立连接成功
    #注意：client_service只负责等待接受客户端的连接请求，收发信息不使用该socket（套接字）
    #之后使用的是新的socket：即为new_client
    #5.等待到客户端发来的数据
    recv_data = new_client.recv(1024)
    print("接受客户端的数据为：",recv_data.decode('utf-8'))
    #6.返还数据到客户端
    send_content = "问题正在处理中......"
    new_client.send(send_content.encode('utf-8'))
    #关闭服务于客户端socket，表示和客户端终止通信
    new_client.close()
    # #7.关闭服务端 ---->> 表示服务端以后不在等待接受客户端的连接
    client_service.close()

