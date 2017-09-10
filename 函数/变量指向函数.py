foo = abs
print(foo(-10))
# 引入内部函数
import builtins
# builtins.abs = 10
print(builtins.abs)

def add(x, y, f):
  return f(x) + f(y)

print(add(-3, -4, abs))
