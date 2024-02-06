def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            next = array[j + 1]
            if(array[j] > next):
                array[j], array[j + 1] = next, array[j] # Tuple unpacking

def bubble_sort_efficient(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i): # - i because the last element is already sorted
            if(array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j] # Tuple unpacking


array1 = [5, 4, 3, 2, 1]
array2 = [5, 4, 3, 2, 1]


bubble_sort(array1)
bubble_sort_efficient(array2)
print(f'Sorted Array: {array1}') # [1, 2, 3, 4, 5]
print(f'Sorted Array: {array2}') # [1, 2, 3, 4, 5]
