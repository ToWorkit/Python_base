# 一组key的集合，不储存value
# set可以看成数学意义上的无序和无重复元素的集合， 因此两个set可以做数学意义上的交集和并集等操作

set_01 = set([1, 2, 3])
set_02 = set([2, 3, 4])
set_03 = set([1, 1, 2, 2, 3, 4, 4, 5, 6, 6])
print(set_01 & set_02) # 交集 {2，3}
print(set_01 | set_02) # 并集 {1, 2, 3, 4}
print(set_03) # 去重
s = set([4, 3, 2])
# add 添加为一个元素
s.add('abc')
print(s)
# update 拆开添加
s.update('abc')
s.update([12, '22'])
print(s)

a = set([1, 2, 3, 9])
b = set([1, 4, 6, 7, 3])
# 差集(在a里面的，但不在b里)
print(a.difference(b))
# 简写
print(a - b)
# 对称差集(没有同时出现在a, b中的数)
print(a.symmetric_difference(b))
print(a ^ b)
# 超集 (a是否完全包含b)
print(a.issuperset(b))
print(a > b)
# 子级
print(a.issubset(b))
print(a < b)
