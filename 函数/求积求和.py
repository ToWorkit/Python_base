# sum() 函数可以接受一个list或者tuple并求和
print(sum(tuple(range(1, 11)))) 
# 阶乘
from functools import reduce
def prod(x, y):
  return x * y
print(reduce(prod, list(range(1, 11))))
print(float('123.456'))
def foo (x):
  return list(map())
