from main import *

run_cases = [
    (
        "# My Essay\n* How we win\n- How you lose\n* Why you're bad\n",
        "# My Essay\n* How we win\n* Why you're bad\n",
    ),
    (
        "# The Plan\n* Phase 1\n- ???\n- Profit\n* Any questions?\n",
        "# The Plan\n* Phase 1\n* Any questions?\n",
    ),
]

submit_cases = run_cases + [
    ("", ""),
    (
        "# Job Hunt\n* Keep going!\n- Panic\n- Stalk the hiring manager\n",
        "# Job Hunt\n* Keep going!\n",
    ),
    (
        "# My favorite languages\n* Golang\n- Java\n* Python\n",
        "# My favorite languages\n* Golang\n* Python\n",
    ),
]


def test(input_document, expected_output):
    print("---------------------------------")
    print(f"Input document:\n{input_document}")
    print(f"Expected output:\n{expected_output}")
    result = remove_invalid_lines(input_document)
    print(f"Actual output:\n{result}")
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
