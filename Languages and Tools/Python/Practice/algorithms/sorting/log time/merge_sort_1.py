import time
import random


def merge_sort(nums):
    # ?
    if len(nums) < 2:
        return nums

    midpoint = len(nums) // 2
    left, right = nums[:midpoint], nums[midpoint:]
    
    sorted_left_side = merge_sort(left)
    sorted_right_side = merge_sort(right)

    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    # ?
    final_list = []

    # Size of Lists
    first_list_size, second_list_size = len(first), len(second)
    # Index Counters
    i, j = 0, 0
    print(first)
    print(second)
    while i < first_list_size and j < second_list_size:
        if first[i] <= second[j]:
            final_list.append(first[i])
            i += 1
        else:
            final_list.append(second[j])
            j += 1

    if i < first_list_size:
        final_list.extend(first[i:])
    if j < second_list_size:
        final_list.extend(second[j:])

    return final_list
        
        

# don't touch below this line


def benchmark(nums, show_nums):
    start = time.time()
    test(nums, show_nums)
    end = time.time()

    timeout = 1.00

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
    print("====================================")


def test(nums, show_nums):
    res = merge_sort(nums.copy())
    if show_nums:
        print(f"nums: {nums}")
        print(f"sorted: {res}")
    else:
        print(f"len nums: {len(nums)}")
        print(f"len sorted: {len(res)}")
    print("------------------------------------")


def main():
    benchmark(get_nums(10), True)
    benchmark(get_nums(100), True)
    benchmark(get_nums(1000), False)
    benchmark(get_nums(10000), False)


def get_nums(num):
    nums = []
    random.seed(1)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
