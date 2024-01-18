from main import *

run_cases = [
    ([1, 1, 1, 2, 2, 2, 3], [1, 2], [3]),
    ([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8], [9, 10]),
]

submit_cases = run_cases + [
    ([], [], []),
    ([1, 1, 1], [], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], []),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3], []),
    ([1, 2, 3, 4, 5], [1, 2, 3], [4, 5]),
    ([1, 2, 3, 4, 5], [1, 3, 5], [2, 4]),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: first_ids = {input1}, second_ids = {input2}")
    print(f"Expecting: {expected_output}")
    result = find_missing_ids(input1, input2)
    if isinstance(result, list):
        result = sorted(result)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()