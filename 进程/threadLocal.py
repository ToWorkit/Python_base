'''
在多线程环境下，每个线程都有自己的数据，一个线程使用自己的局部变量比使用全局变量要好，因为局部变量只有线程自己能够看到，不会影响其他的线程，而全局变量的修改必须加上锁
局部变量的缺点是传递起来不方便
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431928972981094a382e5584413fa040b46d46cce48e000
'''
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
# 全局对象
import threading
# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
  # 获取当前线程关联的student
  std = local_school.student
  print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
  # 绑定ThreadLocal的student 
  local_school.student = name
  process_student()

# 注意tuple格式的数据只有一个时要加个逗号，不然会报TypeError
t1 = threading.Thread(target=process_thread, args=('LP',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('PL',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
