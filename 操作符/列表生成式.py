# 生成list [1, 2, 3, 4, 5]
print(list(range(1, 6)))
# 生成[1*1, 2*2, 3*3, ..., 10*10]
# 方法一 使用循环
l = []
for item in range(1, 11):
  l.append(item * item)
print(l)
# 方法二 使用列表生成式
print([item * item for item in range(1, 11)])
# 只求偶数的
print([item * item for item in range(1, 11) if item % 2 == 0])
# 两个队列的组合
print([m + n for m in 'ABC' for n in 'XYZ'])
