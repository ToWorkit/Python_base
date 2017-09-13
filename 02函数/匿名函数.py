print(list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 相当于
def f(x):
  return x * x
# 匿名函数 lambda 冒号前的x为参数

f = lambda x : x + x
print(f)
print(f(8))
# 匿名函数作为返回值
def build(x, y):
  return lambda: x * x + y * y

print(build(2, 5))
# 匿名函数
print(build(2, 5)())
