# 文件写入在没有关闭之前会在内存中存储并没有真实写入
# 关闭的时候会自动刷新缓冲区

# 需要在cmd中查看效果

f = open('test.txt', 'w', encoding='utf8')
f.write('Hello')
# 手动刷新缓存区将内容写入磁盘
f.flush()
f.close()

# demo
import sys, time
for i in range(30):
  # 不会换行
  # sys.stdout.write('*') # 先存入缓存区等待30个都存入之后再写入磁盘显示
  # 每次都刷新下缓存区
  # sys.stdout.flush()
  # print('*')
  # print 不换行
  # print("-", end='')
  # print 不换行 刷新
  print('*', end='', flush=True)
  # 实际是 0.1 * 30
  time.sleep(0.1)
