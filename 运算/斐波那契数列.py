def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b
    n = n + 1
  return None
print(fib(12))



# generator函数
def fib_g(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n += 1
  return None
# print(fib_g(12))
g = fib_g(6)
for n in g:
  print(n)


  
