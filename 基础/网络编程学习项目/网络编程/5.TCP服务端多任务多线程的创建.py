import socket
import threading


def new_client_socket(ip_port,true_socket):
    print('新客户：', ip_port)
    # 之后用新的socket来进行信息传输
    """为了保持会话可以加上循环"""
    while True:
        message_recv = true_socket.recv(1024)
        # 若下线则数据为空
        if message_recv:
            print('客户返送的信息为：', message_recv.decode('utf-8'))
            respond = '已知晓您的反馈,正在处理中............'
            true_socket.send(respond.encode('utf-8'))
        else:
            print('客户以下线！')
            true_socket.close()
            break
if __name__ == '__main__':
    #创建服务端的socket
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #解决端口号复用问题：
    service_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #绑定ip和端口号
    service_socket.bind(("192.168.0.107",9090))
    #设置监听
    service_socket.listen(128)
    #设置等待
    while True:
        true_socket,ip_port =service_socket.accept()
        '''创建线程实现多任务的处理，即每接受到一个新用户时就创建一个，单独为这个新用户服务的线程。这样就可以实现为多用户服务'''
        true_work = threading.Thread(target=new_client_socket,args=(ip_port,true_socket),daemon=True)
        #设置守护主线程，主线程退出子线程销毁
        #启动子线程执行
        true_work.start()
    #断开主服务（但是服务器一般不断开，所以可以注销）
    # service_socket.close()






























