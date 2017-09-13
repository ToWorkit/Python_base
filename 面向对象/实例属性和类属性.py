class Student(object):
  def __init__(self, name):
    self.name = name

s = Student('Bob')
s.score = 90
print(s.name)
print(s.score)

# 本身绑定属性
class Su(object):
  name = 'student'

# 创建实例
s = Su()
# 打印name属性，s 实例并没有name属性，所以会继续往下查找class的name属性
print(s.name)
# 打印类的name属性
print(Su.name)
# 实例绑定name属性
s.name ='lp'
# 实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)
# 删除实例的name属性
del s.name
# 再次调用s.name, 由于实例的name属性已经删除，那么就会去找class的name属性
print(s.name)
