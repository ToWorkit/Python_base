import threading
import asyncio
# 协程
@asyncio.coroutine
def hello():
  # 线程
  # 同一线程并发
  # 多个coroutine就可以由一个线程并发执行。
  print('Hello World (%s)' % threading.currentThread())
  yield from asyncio.sleep(1)
  print('Hello again (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
