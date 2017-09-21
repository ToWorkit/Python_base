# 不会写入内存，只做磁盘操作，会自动生成迭代器(next())
# es6 generator yield *
f = open('test_02.txt', 'r', encoding='utf8')
# for 内部会将 f 对象做成一个迭代器， 用一个取一个

num = 0
for i in f:
  num += 1
  if num == 6:
    # 字符串拼接
    i = ''.join([i.strip(), ' <---'])
  print(i.strip())
'''
# 上面的效率要高
for i, v in enumerate(f.readlines()):
  print(i)
'''
