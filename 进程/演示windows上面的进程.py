'''
  创建
'''
from multiprocessing import Process
import os
# 子进程需要执行的代码
def run_proc(name):
  print('Run child process %s (%s) ---' % (name, os.getpid()))
if __name__ == '__main__':
  print('Parent process %s' % os.getpid())
  p = Process(target = run_proc, args = ('test',))
  print('Child process will start')
  # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个process实例，用start()方法启动
  p.start()
  # join() 方法可以等待子进程结束后在继续往下运行，适用于进程间的同步
  p.join()
  print('Child process end')  
