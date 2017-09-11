class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def print_score(self):
    print('%s成绩为%s' %(self.name, self.score))
  def get_grade(self):
    if self.score >= 90:
      return 'A'
    elif self.score >= 60:
      return 'B'     
    else:
      return 'C'  

bart = Student('PL', 90)
lisa = Student('LP', 91)
HL = Student('HL', 9)

bart.print_score()
lisa.print_score()    
bart.favour = 'nv'
print(bart.favour)
print(lisa.get_grade())
print(HL.get_grade())
