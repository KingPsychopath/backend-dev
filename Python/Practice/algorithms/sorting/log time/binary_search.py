
def timer_decorator(func):
    def wrapper(target, arr):
        start = time.time()
        func(target, arr)
        end = time.time()
        print(f'Time Taken {(end - start) * 1000}')
    return wrapper

@timer_decorator
def binary_search(target, arr):
    # ? Binary search is a search algorithm that finds the position of a target value within a sorted array
    # ? Binary search compares the target value to the middle element of the array
    # ? If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half
    # ? This process continues until the target value is found
    # ? If the search ends with the remaining half being empty, the target is not in the array
    # ? Binary search runs in logarithmic time in the worst case, making O(log n) comparisons, where n is the number of elements in the array
    # ? Binary search is faster than linear search except for small arrays
    n = len(arr)
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        midpoint = (lo + hi) // 2
        if arr[midpoint] < target:
            lo = midpoint + 1
        else:
            hi = midpoint - 1

    if lo != n and arr[lo] == target: # because we are using lo = midpoint + 1 and hi = midpoint - 1 we need to check if lo is not equal to n
        # if lo is equal to n then we are out of bounds
        # if lo is not equal to n then we are in bounds
        # if we are in bounds then we need to check if the value at lo is equal to the target
        # if the value at lo is equal to the target then we found the target
        # if the value at lo is not equal to the target then we did not find the target
        # n is the length of the array
        return True
    return False






    







    # don't touch below this line


def benchmark(names_dict, first_name):
    start = time.time()
    test(names_dict, first_name)
    end = time.time()

    timeout = 0.05

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
    print("====================================")


def test(target, arr):
    res = binary_search(target, arr)
    print(f"- len arr: {len(arr)}")
    print(f"- target: {target}")
    print(f"Result: {res}")
    print("------------------------------------")


def main():
    complexity = 2000000
    nums = get_nums(complexity)
    benchmark(int(complexity * 0.2344), nums)
    benchmark(int(complexity * 2), nums)
    benchmark(int(complexity + 1), nums)
    benchmark(int(complexity * 0.765), nums)


def get_nums(num):
    nums = []
    for i in range(num):
        nums.append(i)
    return nums


main()