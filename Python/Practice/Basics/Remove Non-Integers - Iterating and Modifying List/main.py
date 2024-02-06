
# Remove non-integers from a list of integers
def remove_nonints(nums):
    nums2 = nums
    for i in nums2[:]: # nums2[:] creates a copy of nums2
        print(i, type(i))
        if type(i) != int:
            nums2.remove(i)
            print(f'Removing {i}')
    return nums2

# List comprehension
def remove_nonints2(nums):
    return [i for i in nums if type(i) == int]

# List comprehension
def remove_nonints4(nums):
    return [i for i in nums if isinstance(i, int)]

# Filter
def remove_nonints3(nums):
    return list(filter(lambda x: type(x) == int, nums))


# Filter
def remove_nonints5(nums):
    return list(filter(lambda x: isinstance(x, int), nums))
