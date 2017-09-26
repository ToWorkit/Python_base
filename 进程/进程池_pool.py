# pool
'''
对pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close(), 调用close()之后就不能继续添加新的 Process -> 进程 了
'''
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
  # gitpid 进程识别码
  print('Run task %s (%s)' % (name, os.getpid()))
  start = time.time()
  time.sleep(random.random() * 3)
  end = time.time()
  # 0.2f 保留小数点后两位(四舍五入)
  print('Task %s runs %0.2f seconds %f' % (name, (end - start), (end - start)))
if __name__ == '__main__':
  print('Parent process %s' % os.getpid())
  p = Pool(4)
  for i in range(5):
    p.apply_async(long_time_task, args=(i,))
  print('Waiting for all subprocesses done')
  p.close()
  p.join()
  print('All subprocesses done')  
