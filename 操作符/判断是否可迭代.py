# 通过collections模块的iterable(可迭代)类型判断
# 引入
from collections import Iterable
# 判断 参数1 的类型是否是 参数2
print(isinstance('ABC', str))
# 判断字符串是否可迭代  True
print(isinstance('abc', Iterable))
# 判断list是否可迭代 True
print(isinstance([1, 2, 3], Iterable))
# 判断tuple是否可迭代 True
print(isinstance((1, 2, 3), Iterable))
# 判断dict是否可迭代 True
print(isinstance({'name': 'pl', 'favour': 'girl'}, Iterable))
# 判断整数是否可迭代 False
print(isinstance(123, Iterable))
