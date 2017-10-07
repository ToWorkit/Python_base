def f(n):
  return n*n
print(f(2))

# 函数作为参数
def foo(a, b, func):
  return func(a) + func(b)
print(foo(2, 3, f))
