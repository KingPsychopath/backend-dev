test_array = [1, 2, 3, 4, 5]
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1 # not found  # O(n)
    
print(f'Index: {linear_search(test_array, 3)}') # 2    