# __getitem__
class Fib(object):
  def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
      a, b = b, a + b
    return a
f = Fib()
# print(f.__getitem__(10))
print(f[10])
# list 数据的切片方法
print(list(range(10))[5:10])
# 需要判断__getitem_-() 传入的参数可能是int，也可能是一个切片对象slice
class Fib(object):
  def __getitem__(self, n):
    # n 是索引 
    if isinstance(n, int):
      a, b = 1, 2
      for x in range(n):
        a, b = b, a + b
      return a
    # n 是切片  
    if isinstance(n, slice):
      start = n.start
      stop = n.stop
      if start is None:
        start = 0
      a, b = 1, 2
      L = []
      for x in range(stop):
        if x >= start:
          L.append(a)
        a, b = b, a + b
      return L
f = Fib()
print(f[0:5])
print(f[:10])
