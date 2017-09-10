# 第一种
print([x * x for x in range(10)])
g = (x * x for x in range(10))
print(next(g)) # 通过next() 函数获得generator的下一个返回值
for n in g:
  print(n)
