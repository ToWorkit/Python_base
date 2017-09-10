# 删掉偶数只保留奇数
def is_odd(n):
  return n % 2 == 1 
print(list(filter(is_odd, range(1, 11))))
# 将一个序列中的空字符串删掉
def not_empty(x):
  return x and x.strip()
print(list(filter(not_empty, [' A', '  b', '', None,'  '])))
print('  n'.strip())
