from main import *

run_cases = [
    ("Hello there", "HHeelllloo  tthheerree"),
    ("General Kenobi", "GGeenneerraall  KKeennoobbii"),
]

submit_cases = run_cases + [
    ("I am an alien", "II  aamm  aann  aalliieenn"),
    ("Python is fun", "PPyytthhoonn  iiss  ffuunn"),
    ("I love coding", "II  lloovvee  ccooddiinngg"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = double_string(input1)
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