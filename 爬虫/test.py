import multiprocessing
import time

# def process(num):
#     time.sleep(num)
#     print ('Process:', num)
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#
#     print('CPU number:' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child process name: ' + p.name + ' id: ' + str(p.pid))
#
#     print('Process Ended')



# def dance(num):
#     time.sleep(num)
#     print(f'小明在跳舞:{num}秒')
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         process_dance = multiprocessing.Process(target=dance,args=(i,))
#         process_dance.start()
#
#     print('跳了多久，cpu_count:',multiprocessing.cpu_count())
#     print(multiprocessing.active_children())



# class MyProcess(multiprocessing.Process):
#     def __init__(self,loop):
#         multiprocessing.Process.__init__(self)
#         self._loop = loop
#
#     def run(self):
#         for i in range(self._loop):
#             time.sleep(i)
#             print('name:',self.pid)
#
# if __name__ == "__main__":
#     for i in range(2,5):
#         a = MyProcess(i)
#         a.start()
#         a.join()
#     print('end')



# import multiprocessing
# import time
#
# print("==== 模块被加载了 ====")
#
# class MyProcess(multiprocessing.Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print(f"【子进程】{self.name} 开始工作，pid:{self.pid}")
#         time.sleep(1)
#         print(f"【子进程】{self.name} 工作结束")
#
# class MyProcess2(multiprocessing.Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('执行统计任务')
#
# # 执行到 if __name__ == "__main__" 时，子进程不会进入这个代码块
# if __name__ == "__main__":
#     print("主线程开始创建进程")
#     p1 = MyProcess("进程1")
#     p2 = MyProcess("进程2")
#     p3 = MyProcess2('进程3')
#
#
#     p3.start()
#     p1.start()
#     p2.start()
#     print("主线程：已经启动两个进程，等待它们结束")
#     p1.join()
#     p2.join()
#     p3.join()
#     print("主线程：所有进程全部完成")



from multiprocessing import Process, Lock
import time


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
            self.lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()























