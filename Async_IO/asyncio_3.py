#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090954004980bd351f2cd4cc18c9e6c06d855c498000

# 用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
# 3个连接由一个线程通过coroutine并发完成。
import asyncio

@asyncio.coroutine
def wget(host):
  print('wget %s' % host)
  connect = asyncio.open_connection(host, 80)
  reader, writer = yield from connect
  header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
  writer.write(header.encode('utf-8'))
  yield from writer.drain()
  while True:
    line = yield from reader.readline()
    if line == b'\r\n':
      break
    print('%s header --> %s' % (host, line.decode('utf-8').rstrip()))  
  writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.baidu.com', 'www.163.com', 'www.sohu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
