import random


def bubble_sort(nums):
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
    return nums


# don't touch below this line


def test(nums):
    res = bubble_sort(nums.copy())
    print(f"nums: {nums}")
    print(f"sorted: {res}")
    print("====================================")


def main():
    test(get_nums(10))
    test(get_nums(100))
    test(get_nums(500))


def get_nums(num):
    nums = []
    random.seed(0)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()