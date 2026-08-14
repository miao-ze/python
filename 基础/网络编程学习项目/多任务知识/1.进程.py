# 【多进程的使用】
# 1.导入进程包
import multiprocessing
import time
import os       #用来获取进程编号用的
'''一:实例一（主进程执行唱歌，创建子进程执行跳舞任务）'''
# 2.创建子进程（跳舞）
# def dance():
#     for i in range(5):
#         print("跳舞中........2")
#         time.sleep(3)
# dance_process = multiprocessing.Process(target=dance) #target要么是一个函数，要么是一个方法{对应的是子进程的对象}
# # 3.创建主进程（唱歌）
# def sing():
#     for i in range(5):
#         print("唱歌中........1")
#         time.sleep(0.3)
# if __name__ == "__main__":  # 在Windows 系统中使用 multiprocessing模块创建子进程时,
#                             # 需要在主模块中添加 if __name__ == '__main__': 条件判断来避免重复执行代码
#     #启动子进程(类名.start())
#     dance_process.start()
#     #启动主进程
#     sing()
# '''一:实例二（主进程创建两个子进程，分别执行唱歌和跳舞）'''
# def dance():
#     for i in range(5):
#         print("跳舞中........2")
#         time.sleep(0.3)
# def sing():
#     for i in range(5):
#         print("唱歌中........1")
#         time.sleep(0.3)
# if __name__ == "__main__":
#     # 创建两个子进程
#     sing_process = multiprocessing.Process(target=sing)
#     dance_process = multiprocessing.Process(target=dance)
#     # 用start执行指点进程对应的任务
#     dance_process.start()
#     sing_process.start()
#
#
#
# #【获取进程编号】
# def dance():
#     # 获取当前进程编号（现在由于是在子进程中所以获取的是子进程的编号）
#     dance_process_id = os.getpid()
#     print('当前进程(子进程dance)进程的id为：',dance_process_id)
#     # 获取当前进程父进程的id
#     dance_process_parent__id = os.getppid()
#     print('当前进程(子进程dance)父进程的id为：',dance_process_parent__id)
#     for i in range(3):
#         print("跳舞中........2")
#         time.sleep(0.2)
# def sing():
#     # 获取当前进程编号（现在由于是在子进程中所以获取的是子进程的编号）
#     sing_process_id = os.getpid()
#     print('当前进程(子进程)sing进程的id为：',sing_process_id)
#     for i in range(3):
#         print("唱歌中........1")
#         time.sleep(0.2)
#         #拓展：通过进程编号强制杀死进程
#         os.kill(sing_process_id,9) #9-->只执行一次就不执行
# #创建两个子进程
# sing_process = multiprocessing.Process(target=sing)
# dance_process = multiprocessing.Process(target=dance)
# #获取当前进程编号（现在由于是在主进程中所以获取的是主进程的编号）
# # mian_process = os.getpid()
# # print("当前进程（现在为主进程）的编号是：",mian_process)
# if __name__ == "__main__":
#     mian_process = os.getpid()
#     print("当前进程（现在为主进程）的编号是：", mian_process)
#
#     print(sing_process)     #可查看此进程的信息如：因为没有设置name参数所以此时默认名字为‘Process-1’
#     print(dance_process)    ##可查看此进程的信息如：因为没有设置name参数所以此时默认名字为‘Process-2’
#     mian_process = os.getpid()
#     sing_process.start()
#     dance_process.start()
#
#
#
# #【进程中带有参数的任务】
# # 方法：1.args元组形式传递 2.kwargs字典形式传递
# # 一.args形式传递
# def i(name,age):
#     print(f'我的名字是{name}，今年{age}岁了。')
# i_process = multiprocessing.Process(target=i,args=('缪泽平',20))
# if __name__ == "__main__":
#     i_process.start()
# # 二.kwargs形式传递
# def i(name,age):
#     print(f'我的名字是{name}，今年{age}岁了。')
# i_process1 = multiprocessing.Process(target=i,kwargs={'name':"lily","age":19})
# if __name__ == "__main__":
#     i_process1.start()
# # 通过input输入参数
# def i(name,age):
#     print(f'我的名字是{name}，今年{age}岁了。')
# if __name__ == "__main__":
#     name = input('请输入您的名字：')
#     #此时在内部创建子进程
#     i_process1 = multiprocessing.Process(target=i, kwargs={'name': name, "age": 19})
#     #在执行创建的子进程
#     i_process1.start()
#
#
# # 进程的注意点：
# # 【1.进程之间不共享全局变量】
# aal_list = []   #定义全局变量列表
# def add_list():
#     for i in range(3):
#         aal_list.append(i)
#         print('添加:',i)
#         time.sleep(0.4)
#     print('添加完成：',aal_list)
# def read_list():
#     print(aal_list)
# '''
# # 提示:对应linux和mac主进程执行的代码不会进程拷贝,但是对window系统来说主进程执行的代码也会进行拷贝执行,
# # 对应window来说创建子进程的代码如果进程拷贝执行相当于递归无限制进行创建子进程,会报错.
# # 所以解决windows递归创建子进程，通过判断是否是主模块来解决即：if __name__ == '__main__':
# # '''
# if __name__ == '__main__':
#     #创建子进程
#     add_list_process = multiprocessing.Process(target=add_list)    #添加数据
#     real_list_process = multiprocessing.Process(target=read_list)  #读取数据
#     #启动进程执行对应的任务
#     add_list_process.start()
#     add_list_process.join()     #等上一个子进程结束在执行下一个进程
#     real_list_process.start()
#     print(aal_list)


# 【2.主进程会等待所有的子进程执行完成以后在退出】
# def i():
#     for i in range(10):
#         print("执行中........")
#         time.sleep(0.2)
# if __name__ == '__main__':
#     i_process = multiprocessing.Process(target=i)
#     i_process.start()
#     time.sleep(0.5)
#     print('over')   #只有在子进程结束是才会退出程序


#【3.强制退出的方法】
def i():
    for i in range(10):
        print("执行中........")
        time.sleep(0.2)
if __name__ == '__main__':
    i_process = multiprocessing.Process(target=i,daemon=True)
    current_main = multiprocessing.current_process()
    print(i_process)
    print(current_main)
    # i_process.daemon = True #(方法一：）把子进程设置为守护主进程,以后主进程退出直接销毁)
    i_process.start()
    time.sleep(0.5)
    # i_process.terminate()     #(方法二：)退出主进程之前，先让子进程进行销毁
    print('over')   #只有在子进程结束是才会执行over
    i_process.terminate()























