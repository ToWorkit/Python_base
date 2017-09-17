# dict(相当于JavaScript的map)，使用键-值(kay-value)存储
# 字典
# 无序， 键唯一
data = {
    'Michael': 90,
    'Bob': 89,
    'Tracy': 98
}
print(data['Bob'])

# 判断key是否存在
# in
print('adc' in data) # False
print('Bob' in data) # True
# get
# 如果key不存在可以返回None或者自己指定的value
print(data.get('abc')) # None
print(data.get('abc'), -1) # -1
print(data.get('Bob')) # 89

# list 和 dict
# list 可以理解为js的数组，根据索引查询值，处理慢，查找和插入的时间随着元素的增加而增加
# dict 是键值对的方式，处理快，不会随着key的增加而变慢，需要占用大量的内存，内存浪费多
#       key必须是不可变对象，通过key计算位置的算法成为哈希算法

# 字典的第二种创建方式
dic = dict((('name', 'lp'), ('age', 24)))
dic_02 = dict([['name', 'pl'], ['age', 24]])
print(dic)
print(dic_02)
