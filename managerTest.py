# import random, time, queue
#
# from multiprocessing.managers import BaseManager
#
# #发送任务队列
# task_queue = queue.Queue()
#
# #接受结果队列
# result_queue = queue.Queue()
#
# class QueueManager(BaseManager):
#     pass
#
# # 把两个queue注册到网络上，callable参数关联queue
# QueueManager.register('get_task_queue', callable=lambda : task_queue)
# QueueManager.register('get_result_queue', callable=lambda :result_queue)
#
# #绑定端口5000，验证码abc
# manager = QueueManager(address=('',5000),authkey=b'abc')
# #启动queue
# manager.start()
# #通过网络访问queue
# task = manager.get_task_queue()
# result = manager.get_result_queue()
#
# #放入任务
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
#
# #从result读取结果
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout = 10)
#     print('Result: %s '% r)
#
# #关闭
# manager.shutdown()
# print('master exit.')

import random, time, queue
from multiprocessing.managers import BaseManager
 # 发送任务的队列:
task_queue = queue.Queue()
 # 接收结果的队列:
result_queue = queue.Queue()

 # 自定义函数re_task_queue
def re_task_queue():
     global task_queue
     return task_queue

 # 自定义函数re_result_queue
def re_result_queue():
     global result_queue
     return result_queue

 # 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':

     # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
     QueueManager.register('get_task_queue', callable=re_task_queue)
     QueueManager.register('get_result_queue', callable=re_result_queue)

     # 绑定端口5000, 设置验证码‘abc‘:
     manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

     # 启动Queue:
     manager.start()

     # 获得通过网络访问的Queue对象:
     task = manager.get_task_queue()
     result = manager.get_result_queue()

     # 放几个任务进去:
     for i in range(10):
         n = random.randint(0, 10000)
         print('Put task %d...' % n)
         task.put(n)

     # 从result队列读取结果:
     print('Try get results...')
     for i in range(10):
         r = result.get(timeout=10)
         print('Result: %s' % r)

     # 关闭:
     manager.shutdown()
     print('master exit.')
