
import socket
if __name__ == '__main__':
    #1.创建TCP客户端的套接节（socket）         【导入socket模块中的socket类】
    #AF_INET : IPV4地址类型
    #SOCK_STREAM :  TCP传输协议类型
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # AF_INET的中文名称是 “地址族因特网”（ip地址类型）,SOCK_STREAM（流式套接字）{所选择的传输协议}
    #2.和服务端套接字连接 ---> 这需要知道服务端的IP地址和端口号（用connect方法--》以元组的形式传递）
    client_socket.connect(("192.168.0.107",9090)) #注意端头号不要加引号
    #3.发送数据到服务端  用send方法
    '''因为信息数据在网络中传播中是以二进制的字节流的形式传播的，所以在发送时要转化为字节形式 **windows里面的网络调试助手使用的是gbk'''

    send_content = input('请输入你的问题：')
    send_data = send_content.encode('utf-8')
    client_socket.send(send_data)
    #4.接受服务端的数据
    reverse_data = client_socket.recv(1024) #1024:表示每次接受的最大字节数  用于接收到的数据是二进制的数据所以要进行解码
    if len(reverse_data) == 0:          #进行判断如果服务端断开连接时返回的数据长度为0
        client_socket.close()
    else:
        print("接收到数据为：",reverse_data.decode('utf-8'))
    #5.结束连接
    client_socket.close()