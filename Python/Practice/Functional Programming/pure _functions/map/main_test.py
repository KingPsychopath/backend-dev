from main import *

run_cases = [
    (
        "# My Essay\n- How we win\n- How you lose\n- Why you're bad mega-person\n",
        "# My Essay\n* How we win\n* How you lose\n* Why you're bad mega-person\n",
    ),
    (
        "# The Plan\n- Phase 1\n- ???\n- Profit\nAny questions?\n",
        "# The Plan\n* Phase 1\n* ???\n* Profit\nAny questions?\n",
    ),
]

submit_cases = run_cases + [
    ("", ""),
    ("-", "*"),
    ("- Single line test\n", "* Single line test\n"),
    (
        "# No changes needed\n* This is fine\n* This too\n",
        "# No changes needed\n* This is fine\n* This too\n",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n{input1}")
    print(f"Expecting:\n{expected_output}")
    result = change_bullet_style(input1)
    print(f"Actual:\n{result}")
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
