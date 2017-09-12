class Animal(object):
  def run(self):
    print('Animal is running')

class Dog(Animal):
  def run(self):
    print('dog')

class Cat(Animal):
  def run(self):
    print('cat')

dog = Dog()
dog.run()
cat = Cat()
cat.run()
