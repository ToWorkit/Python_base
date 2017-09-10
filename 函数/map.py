def foo(x):
  return x * x
# map的第二個參數必须是Iterable(可迭代)
print(list(map(foo, range(1, 10))))  
# 将 list 中的所有数字转为字符串
print(list(map(str, range(1, 10))))
