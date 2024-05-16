for _index, i in enumerate(range(0, 10)):
  print(i, _index)


dictA = {'a': 1, 'b': 2, 'c': 3}
print(dictA['a'])

class1 = ['Join', 'Tom', 'Jerry']
class2 = ['Tom', 'Jerry', 'Join']
class3 = [x for x in class1 if x in class2]
print(class3)
