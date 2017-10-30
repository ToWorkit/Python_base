# 多任务可以由多进程完成，也可以由一个进程内的多线程完成
# 进程由若干线程组成，一个进程至少有一个线程
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
'''
import time, threading
# 新线程执行
def loop():
  # MainThread  主线程
  print('thread %s is running' % threading.current_thread().name)
  n = 0
  while n < 5:
    n += 1
    # LoopThread 循环线程
    print('thread %s ---> %s' % (threading.current_thread().name, n))
    time.sleep(1)
  print('thread %s ended_while' % threading.current_thread().name)  
print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
# 继续执行
# 阻塞进程，直到当前线程执行完毕
t.join()
print('thread %s ended' % threading.current_thread().name)
