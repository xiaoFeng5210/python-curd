for _index, i in enumerate(range(0, 10)):
  print(i, _index)


dictA = {'a': 1, 'b': 2, 'c': 3}
# print(dictA['a'])

class1 = ['Join', 'Tom', 'Jerry']
class2 = ['Tom', 'Jerry', 'Join']
class3 = [x for x in class1 if x in class2]
# print(class3)

class Animal:
  def __init__(self, name):
    print('Animal __init__')
    self.name = name

  def run(self):
    print(self.name, 'is running')

  def eat(self):
    print(self.name, 'is eating')

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)
    print('Dog __init__')

  def bark(self):
    print(self.name, 'is barking')

dog = Dog('dog')
print(dog.eat())
