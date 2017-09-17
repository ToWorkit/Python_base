a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 查
print(a[-1::-3])
print(a[1:5])
print('lp' in a) # False
# 增加
a.append('ll')
print(a)
a.insert(2, '30k')
print(a)
# 可以直接赋值来修改
# 删
a.remove('b') # 根据内容移除
print(a)
# 不指定索引默认删除最后一个
a.pop(3) # 根据索引移除，返回值为删除的元素
print(a)
# del 可以删除 a 这个list本身
del a[0]
print(a)
# clear 清空
a.clear()
print(a)
