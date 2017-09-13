def count():
  fs = []
  for i in range(1, 4):
    def f():
      return i * i
    fs.append(f)
  return fs  
f1, f2, f3 = count()      
# ll = list(range(1, 4))
# 结果应该是1， 4， 9 但实际是 9, 9, 9 
print(f1())
print(f2())
print(f3())
print('-------------')
# 闭包版
def count_():
  def f(j):
    def g():
      return j * j
    return g
  fs = []
  for i in range(1, 4):
    # f(i) 会立刻执行，因此 i 的当前值被传入 f()
    fs.append(f(i))
  return fs  
f1, f2, f3 = count_()
print(f1())
print(f2())
print(f3())
