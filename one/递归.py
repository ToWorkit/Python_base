def fact(n):
    if n == 1:
      return 1
    return n * fact(n - 1)  
# 注意去看尾调用的
print(fact(3))

def foo(n, p = 1):
  if n == 1:
    return p
  return foo(n - 1, n * p)  
print(foo(4))


def fact(n, p = 1):
  if n <= 1:
    return p
  # n * p 在函数调用之前就计算了，不会影响函数调用
  return fact(n - 1, n * p)

print(fact(5))   
