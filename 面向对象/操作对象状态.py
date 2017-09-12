class MyObject(object):
  def __init__(self):
    self.x = 9
  def power(self):
    return self.x * self.x
obj = MyObject()

# 是否有该属性
print(hasattr(obj, 'x'))
print(obj.x)
# 设置一个属性 y
setattr(obj, 'y', '20')
print(getattr(obj, 'y'))
# 从文件流fp中读取图像，首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
# 有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
def readImage(fp):
  if hasattr(fp, 'read'):
    return readData(fp)
  return None  
