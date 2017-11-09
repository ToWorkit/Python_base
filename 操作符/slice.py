l = ['A', 'B', 'C', 'D']
# 取前三个元素 0, 1, 2, 索引为0时可以省略
# print(l[0:3])
print(l[:2])
print(l[1:3])
print(l[:])
# 倒数切片(slice)
print(l[-2:])
print(l[-2:-1])
# 注意查看区别
print(tuple(range(10)))
print(list(range(10)))

num = list(range(100))
# 前十个数，每两个取一个
print(num[:10:2])
# 所有数，每5个取一个
print(num[::5])
# tuple格式和字符串的数据同样适用切片
a = 'abc'
print(a[:1].upper() + a[1:])
