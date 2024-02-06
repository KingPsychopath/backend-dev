list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Split list2 in half
midpoint_index = len(list2) // 2
left = list2[:midpoint_index]
right = list2[midpoint_index:]
print(left)
print(right)

for item1, item2 in zip(list1, list2):
    print(f"Item from list1: {item1}, Item from list2: {item2}")