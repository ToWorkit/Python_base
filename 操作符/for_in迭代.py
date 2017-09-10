# dict 对象
d = {
  'name': 'pl',
  'age': 24,
  'favour': 'girl'
}
for key in d:   # 迭代key
  print(key)
for value in d.values(): # 迭代value
  print(value)
for key, value in d.items(): # 同时迭代key和value
  print(key, '->', value)
