# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000

import asyncio

@asyncio.coroutine
def hello():
  print('Hello World')
  # 异步调用asyncio.sleep(1)
  r = yield from asyncio.sleep(1)
  print("Hello again")

# 获取EventLoop(事件循环)
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
