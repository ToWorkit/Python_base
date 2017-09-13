class Student(object):
  pass
# 实例
s = Student()
# 动态给实例绑定一个属性
s.name = 'lp'
print(s.name)
# 绑定一个方法
# 定义一个函数作为实例方法
def set_age(self, age):
  self.age = age

from types import MethodType
# 给实例绑定有一个方法
s.set_age = MethodType(set_age, s)
# 调用实例方法
s.set_age(25)
print(s.age)
# 注意点：给一个实例绑定的方法无法实现共用
s_02 = Student()
# print(s_02.age) # object has no attribute

# 给class绑定方法可以实现实例共用
def set_score(self, score):
  self.score = score

Student.set_score = set_score
s.set_score(90)
print(s.score) 

### 使用 __slots__

# 限制实例的属性
class Stu(object):
  # 用 tuple 类型定义允许绑定的属性名称
  __slots__ = ('name', 'age')
# 创建实例
t = Stu()
t.name = 'pl'
t.age = 26
# t.score = 99 # 报错  'Stu' object has on attribute 'score'
# 仅对当前类实例起作用，对继承的子类不起作用
class GraduateStudent(Stu):
  pass
g = GraduateStudent()
g.score = 90 # 不会报错  
t.score = 90 # 报错，不允许设置
