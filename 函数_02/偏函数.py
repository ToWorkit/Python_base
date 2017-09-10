# init 会将字符串默认以十进制转换
print(int('123'))
# 通过base参数可以做N进制转换
print(int('123', base = 8))
print(int('123', 9))
# 默认转 二进制 函数
def int2(x, base = 2):
  return int(x, base)
print(int2('1000000000'))

#### 偏函数
import functools
int2 = functools.partial(int, base = 2)
print(int2('1000000'))
print(int2('1000000', base = 10))
