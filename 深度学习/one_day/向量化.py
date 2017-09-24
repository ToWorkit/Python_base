# 向量化可以解决代码中显示使用for循环
# 非向量化的方式
import numpy as np
a = np.array([1, 2, 3, 4])
print(a)

l1 = 2
l2 = 4
print(np.dot(l1, l2))
print(np.random.rand(4))

import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)
# 向量化
# 开始时间
tic = time.time()
c = np.dot(a, b)
# 结束时间
toc = time.time()
print(c)
print('Vectorized version:' + str(1000 * (toc - tic)) + 'ms')

# 非向量化
c = 0
tic = time.time()
for i in range(1000000):
  c += a[i] * b[i]
toc = time.time()
print(c)
print('For loop:' + str(1000 * (toc - tic)) + 'ms')
