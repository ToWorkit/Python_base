class Student(object):
  def __init__(self, name, score, age):
    self.__name = name
    self.__score = score
    self.age = age
  def print_score(self):
    print('%s成绩%s' %(self.__name, self.__score))  
bart = Student('lp', 100, 25)
bart.print_score()
print(bart.age)
bart.age = 26
print(bart.age)
print(bart._Student__name)
print(bart.name)
