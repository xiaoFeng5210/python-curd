a = ['jack', 'john', 'jill', 'jane']
astr = a[:2]

a[0] = 'jim'

b = a
b[1] = 'joe'
print(a)
print(type(b))

