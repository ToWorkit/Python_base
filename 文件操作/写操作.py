# f = open('test.txt', 'w', encoding = 'utf8')
# data = 'Hello Pl'
# f.write(data)
# f.close()
import time
# 有则写入无则创建
with open('test_02.txt', 'w', encoding = "utf8") as f:
  # 不会覆盖
  f.write('Lp Love You\n')
# 5秒之后追加数据
time.sleep(5)
f = open('test_02.txt', 'a', encoding = 'utf8')
f.write('\nMy Love Lp')
f.close()
