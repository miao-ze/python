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



# from multiprocessing import Process, Lock
# import time
#
# class MyProcess(Process):
#     def __init__(self, loop, lock):
#         Process.__init__(self)
#         self.loop = loop
#         self.lock = lock
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(0.1)
#             self.lock.acquire()
#             print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
#             self.lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10, 15):
#         p = MyProcess(i, lock)
#         p.start()



# from multiprocessing import Process, Semaphore, Lock, Queue
# import time
#
# class Consumer(Process):
#     def __init__(self, buffer, empty, full, lock):
#         super().__init__()
#         self.buffer = buffer
#         self.empty = empty
#         self.full = full
#         self.lock = lock
#
#     def run(self):
#         print('子进程二')
#         while True:  # 必须加上死循环
#             self.full.acquire()  # 等待缓冲区有数据（信号量 full > 0）
#             self.lock.acquire()  # 加锁
#             item = self.buffer.get()  # 从队列取出数据
#             print(f'Consumer consumed: {item}')  # 打印消费结果
#             self.lock.release()  # 释放锁
#             self.empty.release()  # 释放一个空位（信号量 empty 加 1）
#
#
# class Producer(Process):
#     def __init__(self, buffer, empty, full, lock):
#         super().__init__()
#         self.buffer = buffer
#         self.empty = empty
#         self.full = full
#         self.lock = lock
#
#     def run(self):
#         print('子进程一')
#         while True:
#             self.empty.acquire()
#             self.lock.acquire()
#             self.buffer.put(1)
#             print('Producer append an element')
#             self.lock.release()  # ✅ 这里先释放锁
#             self.full.release()  # ✅ 再增加信号量通知消费者
#             time.sleep(1)  # ✅ 在锁释放之后，再进行休眠
#
# if __name__ == '__main__':
#     buffer = Queue(10)
#     empty = Semaphore(10)
#     full = Semaphore(0)
#     lock = Lock()
#     p = Producer(buffer=buffer,empty=empty,full=full,lock=lock)
#     c = Consumer(buffer=buffer,empty=empty,full=full,lock=lock)
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print ('Ended!')



# from multiprocessing import Process, Pipe
# import time
#
# class Consumer(Process):
#     def __init__(self, num, pipe_recv):
#         super().__init__()
#         self.num = num
#         self.pipe_recv = pipe_recv  # 接收端
#
#     def run(self):
#         print('子进程二 (消费者) 已启动')
#         for _ in range(self.num):
#             # 从管道接收数据 (recv 会阻塞等待数据)
#             item = self.pipe_recv.recv()
#             print(f'消费者接收并打印: {item}')
#         print('消费者接收完毕')
#
#
# class Producer(Process):
#     def __init__(self, num, pipe_send):
#         super().__init__()
#         self.num = num
#         self.pipe_send = pipe_send  # 发送端
#
#     def run(self):
#         print('子进程一 (生产者) 已启动')
#         for i in range(self.num):
#             # 将数据发送到管道
#             self.pipe_send.send(f'数据-{i}')
#             print(f'生产者发送了: 数据-{i}')
#             time.sleep(1)  # 模拟生产数据的时间
#         # 发送完毕后关闭发送端（让消费者端的 recv 不会陷入死等）
#         self.pipe_send.close()
#
#
# if __name__ == '__main__':
#     # 创建单向管道：pipe_recv 只能读，pipe_send 只能写
#     pipe_recv, pipe_send = Pipe(duplex=False)
#
#     # 【最关键的一步】把对应的端点传给各自的进程
#     p = Producer(num=5, pipe_send=pipe_send)
#     c = Consumer(num=5, pipe_recv=pipe_recv)
#
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#
#     p.join()
#     c.join()
#     print('Ended! 主程序退出')




# from multiprocessing import Lock, Pool
# import time
#
# def function(index):
#     print ('Start process: ', index)
#     time.sleep(3)
#     print ('End process', index)
#
#
# if __name__ == '__main__':
#     pool = Pool(processes=3)
#     for i in range(4):
#         pool.apply_async(function, (i,))
#
#     print ("Started processes")
#     pool.close()
#     pool.join()
#     print ("Subprocess done.")

# print('test')

# import re
#
# with open('资料文件\\1.html','r',encoding='utf-8') as f:
#     data = f.read()
#     result = re.search(r'<a\s.*?href="(.*?)"\sclass="name">',data)
#     print(result.group(1))


import requests
import re

# headers = {'Cookies':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}
# res = requests.get('https://lzacg.cc/category/galgame/page/1',headers=headers)

# with open('资料文件\\lzacg.html','w',encoding='utf-8') as f:
#     f.write(res.text)

# url_picture_name = re.compile(r'<posts.*?<a.*?target="_blank".*?href="(.*?)">.*?<img.*?data-src="(.*?)"\salt="(.*?)".*?>',re.S)
#
# if __name__ == "__main__":
#     with open('资料文件\\lzacg.html', 'r', encoding='utf-8') as f:
#         data = f.read()
#         result = re.search(url_picture_name,data)
#         print(result.group(1))
#         print(result.group(2))
#         print(result.group(3))



headers = {'Cookies':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}
# res = requests.get('https://lzacg.cc/11030',headers=headers)

from lxml import etree


# with open('资料文件\\lzacg_detail.html', 'r', encoding='utf-8') as f:
#    data = f.read()

# data = requests.get('https://lzacg.cc/11026')
# with open('资料文件\\lzacg_detail.html', 'w', encoding='utf-8') as f:
#    f.write(data.text)

# html = etree.HTML(data)
# gal = html.xpath('//h4[@class="wp-block-heading"][1]/following-sibling::p/text()')
# print(gal)





# data = requests.get('https://lzacg.cc/10000',headers=headers)
# html = data.text
# html2 = etree.HTML(html)
# 第一个h4之后、第二个h4之前的所有p

# xp2 = '''(//div[contains(@class,"wp-posts-content")]/h4[@class="wp-block-heading"])[1]
# /following-sibling::p[count(preceding-sibling::h4[@class="wp-block-heading"])=1]/text()'''


# p_nodes = html2.xpath('//title/text()')
# print(p_nodes[0].rstrip('-量子ACG'))

# p_nodes2 = html2.xpath('//link[@rel="canonical"]/@href')[0]
# print(p_nodes2)




from bs4 import BeautifulSoup


# res = requests.get('https://lzacg.cc/category/galgame/page/2',headers=headers)
# data = res.text
# soup = BeautifulSoup(data,'lxml')
# print(soup.posts.div.a['href'])
# urls = soup.select('.posts-item.ajax-item.card .item-thumbnail a')
# list1 = [url['href'] for url in urls]
# print(list1)


res = requests.get('https://lzacg.cc/11019',headers=headers)
data = res.text

# soup = BeautifulSoup(data,'lxml')
# img = soup.find(name='figure').find('img')
# print(img['src'])

html = etree.HTML(data)
img_ele = html.find(".//figure/img").get('src')
print(img_ele)