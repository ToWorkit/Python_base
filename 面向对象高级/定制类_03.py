# __getattr__
# 避免调用不存在的方法和属性时报错
class Stu(object):
  def __init__(self):
    self.name = 'LP'
# 实例化
s = Stu()
print(s.name)    
# print(s.score) # 'Stu' object has no attribute 'score'
# 避免错误
class Stu(object):
  def __init__(self, name):
    self.name = name
  def __getattr__(self, attr):
    if attr == 'score':
      return 99
    elif attr == 'age':
      return lambda x : x * x
    raise AttributeError('\'Stu----\' object has no attribute \' %s \'' % attr)
s = Stu('lp')
print(s.name)
print(s.age(9))
# print(s.init)

# __call__
# 对象实例可以有自己的属性和方法，使用 __call__ 在实例本身上调用
class Sen(object):
  def __init__(self, name):
    self.name = name
  def __call__(self):
    print('My name is %s' % self.name)
# 实例
s = Sen('pl')
# 不传入参数
print(s())
# callable
# 通过callable()函数判断一个对象是否是可调用对象
print(callable(Sen))
