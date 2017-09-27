# copy
l = ['a', 'b', 'c']
l2 = l.copy()
l2[0] = 'LP'
print(l)
# l2 的修改不会影响l
print(l2) 

l3 = [[1, 2], 'l', 'p']
l4 = l3.copy()
l4[0][0] = 2
# 深层copy修改则会影响到 l3
print(l3)
print(l4)
