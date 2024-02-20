from main import *

run_cases = [
    ([10, 12, 14], 12),
    ([9, 11, 16, 20], 13.5),
]

submit_cases = run_cases + [
    ([8, 8, 8], 8),
    ([14, 18, 22, 30], 20.0),
    ([6, 6, 6, 24, 24, 24], 15.0),
    ([], None),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_median_font_size(input1)
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
