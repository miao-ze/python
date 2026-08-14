#【多线程的使用】
# 1.导入线程模块
import threading
import time

def sing():
    #获取当前线程 / 函数是threading.current_thread()
    current_thread = threading.current_thread()
    print('当前子线程1(sing):',current_thread)
    for i in range(3):
        print('唱歌中.....')
        time.sleep(0.2)
def dance():    #获取当前线程
    current_thread = threading.current_thread()
    print('当前子线程2(dance):',current_thread)
    for i in range(3):
        print('跳舞中.....')
        time.sleep(0.2)
if __name__ == '__main__':
    #2.创建子线程
    sing_thread = threading.Thread(target=sing,name='sing-thread')
    dance_thread = threading.Thread(target=dance,name='dance-thread')
    print('唱歌：',sing_thread)
    # 3.启动子线程
    sing_thread.start()
    dance_thread.start()


# 【线程执行带参数的任务】
# 和进程传参一样用args或kwargs
def i(name,age):
    print(f'我的名字是{name}，今年{age}岁了')
if __name__ == '__main__':
    name = input('请输入你的名字：')
    age = input("请输入你的年龄：")
    #创建子线程
    xian1 = threading.Thread(target=i,args=(name,age)) #也可以用kwargs以字典的方式传参
    #执行子线程
    xian1.start()


# 【线程的注意点】
'''
线程的注意点介绍:
    1.线程之间执行是无序的
    2.主线程会等待所有的子线程执行结束再结束
    3.线程之间共享全局变量
    4.线程之间共享全局变量数据出现错误问题
'''
# 1.线程之间执行是无序的
# def test1():
#     #获取当前线程
#     print(threading.current_thread())
# if __name__ == '__main__':
#     for i in range(20):
#         text_thread = threading.Thread(target=test1)
#         text_thread.start()
        # 线程之间的执行也是无序的，具体那个线程执行是由cpu调度决定的。
        # 进程之间的执行也是无序的，具体那个线程执行是由操作系统决定的


# 2.主线程会等待所有的子线程执行结束在结束
# def test2():
#     while True:
#         print('任务执行中.......')
#         time.sleep(1)
# if __name__ == '__main__':
#     test1_process = threading.Thread(target=test2,daemon=True) #方案一：daemon=True表示创建子线程守护主线程，主线程退出子线程直接销毁
#     test1_process.start()
#     time.sleep(4)
#     print('over')


# 3.线程之间共享全局变量
# list1 = list()
# def add_text3():
#     for i in range(5):
#         print('添加数据：',i)
#         list1.append(i)
#         time.sleep(0.2)
#     print(list1)
# def read_text3():
#     print('查看list1：',list1)
# if __name__ == '__main__':
#     add_text3_process = threading.Thread(target=add_text3)
#     read_text3_process = threading.Thread(target=read_text3)
#     add_text3_process.start()
#     # time.sleep(2)
#     #让当前线程完成后，代码在执行：
#     add_text3_process.join()
#     read_text3_process.start()


# 4.线程之间共享全局变量数据出现错误问题
# g_num = 0
# #任务一：循环100万次
# def text4():
#     # 注意要声明 因为是不可变类型
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#     print()
#     print(f'text4: {g_num}')
# def text5():
#     # 注意要声明 因为是不可变类型
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#     print()
#     print(f'text5:{g_num}')
# if __name__ == '__main__':
#     #创建两个子线程
#     first_thread = threading.Thread(target=text4)
#     second_thread = threading.Thread(target=text5)
#     #启动线程任务
#     first_thread.start()
#     #线程等待：让第一个线程执行，然后等待第一个子线程完成后在执行下个(这样就不会出问题)
#     first_thread.join()
#     second_thread.start()


# 【互斥锁】对共享数据进行锁定，保证同一时刻只能有一个线程操作
g_num = 0
#任务一：循环100万次
# 创建互斥锁 ，Lock本质上是一个函数
lock = threading.Lock()
def text4():
    # ----------------上锁
    lock.acquire()
    # 注意要声明 因为是不可变类型
    global g_num
    for i in range(1000000):
        g_num += 1
    print()
    print(f'text4: {g_num}')
    # -----------------释放锁
    lock.release()  #一定要释放
def text5():
    lock.acquire()# ----------------上锁
    # 注意要声明 因为是不可变类型
    global g_num
    for i in range(1000000):
        g_num += 1
    print()
    print(f'text5:{g_num}')
    lock.release()#-----------------释放锁
if __name__ == '__main__':
    #创建两个子线程
    first_thread = threading.Thread(target=text4)
    second_thread = threading.Thread(target=text5)
    #启动线程任务
    first_thread.start()
    second_thread.start()
#互斥锁可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的数据没有问题
#线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据的准确性，但是执行效率下降


# 【死锁】：一直等待对方释放锁的情景叫做死锁

#需求： 多线程同时根据下标在列表中取值，要保证同一时刻只能有一个线程去取值
lock = threading.Lock()
def get_value(index):
    lock.acquire()      #上锁
    list1 = [1,3,6]
    if index >= len(list1):
        print("下标越界：", index)
        lock.release()   #此时要加上释放锁
        return           #此时由于return结束了，但是锁并没有释放，这时会被锁死，线程无法结束
    print(list1[index])
    lock.release()      #释放锁
if __name__ == '__main__':
    # 创建10个线程
    for i in range(10):
        print(threading.current_thread())
        get_value_process = threading.Thread(target=get_value,args=(i,)) #注意逗号
        get_value_process.start()












