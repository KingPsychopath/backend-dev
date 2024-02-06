i = [[1], 2]

for n in i:
    print(n)

i.append(i[0] + [2])
print(i)