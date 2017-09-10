import numpy as np
# 矩阵
A = np.array([
    [56.0, 0.0, 4.4, 68.0],
    [1.2, 104.0, 52.0, 8.0],
    [1.8, 135.0, 99.0, 0.9]
  ])
# 竖列求和 (平面对应位置)
# 竖轴为 0， 横轴为 1
cal = A.sum(axis = 0)
print(cal)
# 对应的值除以对应竖列的和 百分比
# 除以1 * 4的矩阵，得到百分比的矩阵
# reshape 确保你的矩阵形状是你想要的
percentage = 100 * A / cal.reshape(1, 4)
print(percentage)
