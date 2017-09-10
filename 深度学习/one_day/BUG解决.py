import numpy as np
# 随机5个高斯变量
# 秩为1 的数组
a = np.random.randn(5)
print(a)
# 矩阵的长度
print(a.shape)
# 转置
print(a.T)
print(np.dot(a, a.T))
# 1 * 5 的矩阵
a = np.random.randn(5, 1)
print(a)
# 注意看区别
print(a.T)
# 矩阵的乘积
print(np.dot(a, a.T))
# 与上面对比，写时不要省略 1
a = np.random.randn(1, 5)
print(a)
