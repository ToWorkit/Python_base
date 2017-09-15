# 操作二进制数据
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 初始化
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# f.read()
# b'\xe4\xb8\xad\xe6\x96\x87'
