'''
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
'''
import time, threading
# 假定数据
balance = 0
# 锁
lock = threading.Lock()

def change_it(n):
  # 先存后取
  global balance
  balance += n
  balance -= n
# 当多个线程同时执行lock.acquire()时，只会有一个线程能成功的获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
def run_thread(n):
  for i in range(1000000):
    # 先要获取锁
    lock.acquire()
    # 获得锁的线程用完之后需要释放，不然就会成为死线程，使用try...finally来确保锁一定会被释放
    try:
      # 修改数据
      change_it(n)
    finally:
      # 改完之后必须要释放锁
      lock.release()
t1 = threading.Thread(target=run_thread, args=(6,))
t2 = threading.Thread(target=run_thread, args=(9,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
