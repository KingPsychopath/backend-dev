# List
a = []
a.append(1)
a.append(2)

print(a)
a.pop(0)
print(a)
a.append(1)
print(a)
a.pop()
print(a)

# List Comprehension
b = [x for x in range(10)]
c = [[0] * 5 for x in range(10)]
d = [[2 for y in range(5)] for x in range(3)]
print(b)
print(c)
print(d)

b = [x for x in range(10)]
print(b)
b = list(filter(lambda x: x % 2 == 0, b))
print(b)
b = list(map(lambda x: x * 2, b))
print(b)
from functools import reduce
b = reduce(lambda x, y: x + y, b)
print(b)

# Generator Expression
b = (x for x in range(10)) 
print(list(b))
# Tuple
a = (1, 2, 3, 4, 5)
print(a)
print(a[0])
print(len(a))
# Set


# Dict