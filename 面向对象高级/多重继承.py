# 多重继承
class Animal(object):
  pass
# 大类
# 哺乳类
class Mammal(Animal):
  pass
# 鸟类
class Bird(Animal):
  pass

# 给动物加上Runnable和Flyable的功能
class Runnable(object):
  def run(self):
    print('Running')
class Flyable(object):
  def fly(self):
    print('Flying')

# 各种动物
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
  pass
# 对于有run功能的动物，就多继承一个Runnable  
class Cat(Mammal, Runnable):
  pass
class Parrot(Bird):
  pass
# 对于有fly功能的动物，多继承一个Flyable  
class Ostrich(Bird, Flyable):
 pass 

# MixIn

