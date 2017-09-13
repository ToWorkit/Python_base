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
