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
