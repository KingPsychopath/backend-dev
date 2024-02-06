'''
In Python, you can calculate how many times a specific size subarray will fit within the elements of an array by using integer division. Here's how you can do it:

In this example, len(arr) gives you the total number of elements in the array, and subarray_size is the size of the subarray you're interested in. The // operator performs integer division, which gives you the number of times the subarray size fits in the total number of elements.

Please note that this calculation gives you the number of non-overlapping subarrays of the specified size that will fit in the array. If the total number of elements is not a multiple of the subarray size, the remaining elements are not counted.


'''
# Define the array and the subarray size
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subarray_size = 3

# Calculate how many times the subarray fits in the array
num_subarrays = len(arr) // subarray_size

print(num_subarrays)  # Output: 3

# Define the array and the subarray size
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subarray_size = 3

# Calculate the number of overlapping subarrays
num_subarrays = len(arr) - subarray_size + 1

print(num_subarrays)  # Output: 7

'''
If you want to calculate the number of overlapping subarrays of size K within an array, you can simply subtract K - 1 from the length of the array. Here's how you can do it:

In this example, len(arr) - subarray_size + 1 gives you the number of overlapping subarrays of size K that fit within the array. This works because each new subarray starts one element after the start of the previous subarray, so you can start a new subarray at each element except the last K - 1 elements.



Here's a step-by-step explanation:

- len(arr) gives you the total number of elements in the array.
- len(arr) - K is the last position in the array where a subarray of size K starts. Any position after this would not have enough elements after it to form a subarray of size K.
- len(arr) - K + 1 is used because the range() function in Python stops one step before the end value. So, to include the position len(arr) - K in the loop, you need to add 1.

So, for i in range(len(arr)-K+1): is a loop that goes through the array from the start to the last position where a subarray of size K can start. For each position i, it considers the subarray of size K that starts at position i.
'''