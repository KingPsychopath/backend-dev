from main import *

run_cases = [
    (0, {"name": "Slayer", "level": 128}),
    (1, {"name": "Dorgoth", "level": 300}),
    (3, "index is too high"),
    (-1, "negative ids not allowed"),
]

submit_cases = run_cases + [
    (2, {"name": "Saruman", "level": 4000}),
    (10, "index is too high"),
    (-5, "negative ids not allowed"),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expecting: {expected_output}")
    result = handle_get_player_record(input)
    print(f"Actual: {result}")
    if isinstance(result, Exception):
        result = f"{result}"
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