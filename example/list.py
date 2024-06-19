a = ['jack', 'john', 'jill', 'jane']
astr = a[:2]

a[0] = 'jim'

b = a
b[1] = 'joe'
print(a)
print(type(b))

a_list = [a for a in range(10) if a == 5 or a == 6]
print(a_list)
