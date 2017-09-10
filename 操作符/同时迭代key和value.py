d = {'x': 'a', 'y': 'b', 'z': 'c'}
print(d.items())
for k, v in d.items():
  print(k, v)
# 使用两个变量来生成list
print([k + '->' + v for k, v in d.items()])
