'''
序列化：变量从内存中变成可存储或传输的过程
反序列化：把变量内容从序列化的对象重新读到内存里
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000
'''
# pickle

# 序列化
# 把一个对象序列化并写入文件
import pickle
d = dict(name = 'LP', age = 26, score = 88)
print(d)

'''
# pickle.dumps() 把对象序列化成一个bytes，然后将bytes写入文件
# pickle.dump() 直接把对象序列化后写入
print(pickle.dumps(d))
f = open('test.txt', 'wb')
pickle.dump(d, f)
f.close()
'''

# 反序列化
'''
  把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
'''
f = open('test.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# 仅仅只是内容一致而已，是两个完全不相干的对象
