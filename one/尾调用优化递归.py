def fact(n, p = 1):
  if n <= 1:
    return p
  # n * p 在函数调用之前就计算了，不会影响函数调用
  return fact(n - 1, n * p)

print(fact(5))   
