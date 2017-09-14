# 原始
class Student(object):
  def __init__(self, name):
    self.name = name
print(Student('lp'))
# 定义 __str__
class Student(object):
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return 'Student object (name: %s)' % self.name
print(Student('LP'))      

s = Student('pp')
print(s)

# __str__() 返回用户看到的字符串
# __repr__() 返回开发看到的字符串 作为调试

class Stu(object):
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return 'Stu object (name -> %s)' % self.name
  __repr__ = __str__
print(Stu('ll'))      


# __iter__
# 使类可以用于for..in循环，该方法返回一个迭代对象
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
  def __init__(self):
    # 初始化两个计数器
    self.a, self.b = 0, 1
  def __iter__(self):
    # 实例本身就是迭代对象，所以返回自己
    return self
  def __next__(self):
    # 计算下一个值
    self.a, self.b = self.b, self.a + self.b  
    # 循环的退出条件
    if self.a > 10:
      raise StopIteration()
    # 返回下一个值  
    return self.a

for n in Fib():
  print(n)
# Fib实力虽然能作用于for循环，很像list但是并不能将它当做list来使用
print(Fib()[5]) # 报错 'Fib' object does not support indexing 

# 需要实现__getitem__() 就可以像list那样按照下标取出元素
