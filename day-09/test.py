a = [0, 2, 1]
b = 1
print(a)
b = b + 2 % 3
a.insert(b, 3)
b = a.index(3)
print(a, b)

b = b + 2 % 4
a.insert(b, 4)
b = a.index(4)
print(a, b)