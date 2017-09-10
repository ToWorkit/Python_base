# 构造一个生成器
def _odd_iter():
  n = 1
  while True:
    n += 2
    yield n
# 筛选函数
def _not_divisible(n):
  return lambda x:x % n > 0
# 定义一个生成器，不断返回下一个素数
def primes():
  yield 2
  it = _odd_iter() # 初始化序列
  while True:
    n = next(it) # 返回序列的第一个数
    yield n
    it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数，因为是生成器是无限序列的，需要设置退出循环的条件
for n in primes():
  if n < 100:
    print(n)
  else:
    break  
