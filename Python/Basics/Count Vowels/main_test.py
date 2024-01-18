from main import *

run_cases = [
    (
        "Building a job-ready portfolio of coding projects does not happen overnight.",
        24,
    ),
    ("Applications are normal programs.", 11),
]

submit_cases = run_cases + [
    ("RANDOM TEXT WITH FEW VOWELS.", 7),
    ("", 0),
    ("A quick brown fox jumps over the lazy dog", 11),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Text: {input1}")
    print(f"Expecting: {expected_output}")
    result = count_vowels(input1)
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
