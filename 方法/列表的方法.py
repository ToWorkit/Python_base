a = [1, 2, 3, 4, 2, 5, 2]

# 判断是不是列表
print(type(a) is list)
# 列表中某一元素出现的次数
print(a.count(2))
b = ['e', 'c', 'b', 'a']
# 合并列表, 会改变a
a.extend(b)
print(a)
# 合并列表，不会改变原列表
c = a + b
print(c)
# 根据内容查找数据
print(a.index('b'))
# 翻转数组
a.reverse()
print(a)
v = [2, 6, 9, 4, 1]
# 排序 (默认从小到大)
v.sort(reverse=True) # 从大到小
print(v)
l = [4, 2, 1, 5]
# 排序，不会影响原始值
m = sorted(l, reverse=True)
print(l)
print(m)
