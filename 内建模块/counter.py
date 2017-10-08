# 统计字符出现的个数
# 也是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'Hello World':
  c[ch] += 1
print(c)  
