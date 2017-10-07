# 用来解决bytes和其他二进制数据类型的转换
import struct
print(struct.pack('>I', 10240099))

