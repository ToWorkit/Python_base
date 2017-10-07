# 摘要算法，MD5， SHA1等
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

# 计算一个字符串的MD5值
import hashlib
md5 = hashlib.md5()
md5.update('Hello World'.encode('utf-8'))
print(md5.hexdigest())
