# 排序 倒序
print(sorted([90, 9, -1, 8, -23]))
# 按绝对值大小排序
print(sorted([90, 9, -1, 8, -23], key = abs))
# 字符串排序，会按照ASCLL码的大小进行比较
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))
# 上面是从小到大的


# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))


# 指定排序

# 单独输入L[0]是列表的第一个对象('Bob', 75)
# 在sorted中是对列表的每一个对象做key函数的处理，相当于是分别取出('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)再取每一个的第一维
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def key(n):
  return n[0]
print(sorted(L, key = key))
def value(n):
  return n[1]
print(sorted(L, key = value, reverse = True))
