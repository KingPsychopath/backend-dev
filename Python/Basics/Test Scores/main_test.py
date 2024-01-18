from main import *

run_cases = [
    (
        ["A", "A", "C", "D", "D", "B", "C", "D"],
        ["A", "B", "C", "A", "D", "B", "C", "D"],
        (75.0),
    )
]

submit_cases = run_cases + [
    (
        ["A", "B", "C", "D", "D", "B", "C"],
        ["A", "B", "C", "D", "D", "B", "C"],
        (100.00),
    ),
    (["A", "B", "C", "D", "D", "B", "C"], ["B", "A", "B", "A", "A", "C", "A"], (0.00)),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nanswer_sheet: {input1}\nstudent_answers: {input2}")
    print(f"Expecting: {expected_output}")
    result = get_test_score(input1, input2)
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