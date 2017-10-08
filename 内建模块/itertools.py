# 操作迭代对象
# 只有用for循环迭代的时候才真正计算。
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200162233153835cfdd1a541a18ddc15059e3ddeec000

import itertools
# 无限的迭代器
# natuals = itertools.count(1)
# for n in natuals:
#   pass
  # print(n)

# 字符串也是序列的一种
# cs = itertools.cycle('abc')
# for c in cs:
#   pass
#   # print(c)

# 把一个元素无限重复下去，第二个参数为限定重复次数
# ns = itertools.repeat('a', 3) # 迭代器
# for n in ns: # 迭代
#   print(n)

# 通过takewhile()等函数根据条件判断来截取一个有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x : x <= 10, natuals)
# ln = list(ns)
# print(ln)

# chain()
# 将一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'xyz'):
  print(c)

# groupby()
# 把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('aaaAAAbbbCCC'):
    print(key, list(group))

# 忽略大小写分组
for key, group in itertools.groupby('aaaAAAbbbCCC', lambda c : c.upper()):
    print(key, list(group))
