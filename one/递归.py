def fact(n):
    if n == 1:
      return 1
    return n * fact(n - 1)  
# 注意去看尾调用的
print(fact(3))
