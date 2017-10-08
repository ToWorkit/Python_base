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
