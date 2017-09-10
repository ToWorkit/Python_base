# enumerate函数可以将list变成索引-元素对，这样就可以使用for循环同时迭代索引和元素本身
for i, v in enumerate(['A', 'B', 'C']):
  print(i, '->', v)

for x, y in [(1, 1), [3, 4], (2, 5), {'favour': 'girl', 'name': 'hl'}]:
    print(x, y)
