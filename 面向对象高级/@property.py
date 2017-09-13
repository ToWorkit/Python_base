# 检查参数
class Student(object):
  def get_score(self):
    return self._score
  def set_score(self, value):
    if not isinstance(value, int): # 校验参数
      raise ValueError('score must be a integer')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100')
    self._score = value
# 注意实例化的时候没有参数    
s = Student()
s.set_score(99)
print(s.get_score())

### 使用 @property
class Stu(object):
  @property
  def score(self):
    return self._score
  @score.setter
  def score(self, value):
    # 校验
    if not isinstance(value, int):
      raise ValueError('score must be an interger')
    if value < 0 or value > 100:
      raise ValueError('score must between 0 - 100')  
    self._score = value
# 可控的属性操作
t = Stu()
# 实际会转化为 t.set_score(90)
t.score = 90
# 实际会转化为 t.get_score()
print(t.score)

# 定义只读属性
class Sd(object):
  @property
  def birth(self):
    return self._birth

  @birth.setter
  def birth(self, value):
      self._birth = value

  @property
  def age(self):
      return 2017 - self._birth

# 实例
d = Sd()
d.birth = 30000
print(d.age)
