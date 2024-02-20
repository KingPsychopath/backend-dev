import time
import random


def merge_sort(nums):
    # ?
    if len(nums) < 2:
        return nums

    midpoint_index = len(nums) // 2
    left = nums[:midpoint_index]
    right = nums[midpoint_index:]
    sorted_left = merge_sort(left) + left
    sorted_right = merge_sort(right) + right

    final_list = merge(sorted_left, sorted_right)
    return final_list


def merge(first, second):
    # ?
    final_list = []
    i, j = 0, 0

    for a, b in zip(first, second):
        print(a)
        print(b)
        if a <= b:
            final_list.append(a)
            i += 1
        else:
            final_list.append(b)
            j += 1

    size = 0
    if(len(first) > len(second)):
        size = len(second)
        first = first[size + 1:]
        final_list.append(first)
    elif len(second) > len(first):
        size = len(first)
        second = second[size + 1:]
        final_list.append(second)

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
