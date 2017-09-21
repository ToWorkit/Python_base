# 不会写入内存，只做磁盘操作，会自动生成迭代器(next())
# es6 generator yield *
f = open('test_02.txt', 'r', encoding='utf8')
# for 内部会将 f 对象做成一个迭代器， 用一个取一个
for i in f:
  print(i.strip())
