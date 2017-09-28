'''
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000
'''
# Queue
# process 进程
# Thread  线程
import random, time, queue
# 分布式
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManger继承的QueueManger
class QueueManager(BaseManager):
  pass

# 将两个Queue都注册到网络上，callable参数关联了Queue对象
# register 寄存器
QueueManager.register('get_task_queue', callable=lambda: task_queue)  
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000，设置验证码为 '123'
# b 表示字节
manager = QueueManager(address=('', 5000), authkey=b'123')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放一些任务
for i in range(10):
  n = random.randint(0, 10000)
  print('Put task %d' % n)
  task.put(n)
# 从result队列中读取结果
print('Try get results')
for i in range(10):
  r = result.get(timeout=10)
  print('Result: %s' % r)
# 关闭
manager.shutdown()
print('master exit')
