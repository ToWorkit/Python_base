# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 利用reduce求序列和
from functools import reduce
def add(x, y):
  return x + y
print(reduce(add, list(item for item in range(1, 10) if item % 2 != 0)))
print(list(item for item in range(1, 10) if item % 2 != 0))

from functools import reduce
def fn(x, y):
  return x * 10 + y
# 将[1, 3, 5, 7, 9]转为13579
print(reduce(fn, [item for item in range(1, 10) if item % 2 != 0]))
