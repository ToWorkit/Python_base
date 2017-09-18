# dict 
# 增加
dic_01 = {'name': 'HL'}
dic_01['age'] = 24 # 有则修改无则增加
print(dic_01)

# 增加 
# 键存在 不修改 返回值
# 键不存在 增加 并返回值
ret = dic_01.setdefault('hobby', 'girl')
print(ret)
print(dic_01)

# 打印所有的键
# dict_keys dict_values 类型， python3做出的优化，为了防止键或者值太多而一次性取出所造成内存的消耗
print(dic_01.keys()) 
# 转换为list列表
print(list(dic_01.keys())) 
# 值
print(dic_01.values())
# 键值对
print(dic_01.items())

# 改
dic_02 = {'name': 'lp', 'hobby': 'boy', 'go': 'world'}
# 更新，有则覆盖， 无则创建
dic_01.update(dic_02)
print(dic_01)
print(dic_02)

# 删
dic_03 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
# 指定删除， 也可以删除整个字典，再取时会报错
del dic_03['c']
print(dic_03)
print(dic_03.pop('b')) # 返回删除的值
print(dic_03)

# 随机删除
reg = dic_03.popitem()
print(reg)
print(dic_03)

# 清空
dic_03.clear()
print(dic_03)


# 新的创建字典
dic_04 = dict.fromkeys(['key1', 'key2', 'key3'], 'test')
print(dic_04)

# 排序 默认根据key
dic_05 = {
  2: '1',
  4: '2',
  1: '3'
}
print(sorted(dic_05.values()))
