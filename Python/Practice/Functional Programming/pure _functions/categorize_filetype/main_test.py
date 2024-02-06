from main import *

run_cases = [
    ("document1.txt", "Text"),
    ("notes.docx", "Document"),
    ("bot.py", "Code"),
    ("unknown.xyz", "Unknown"),
]

submit_cases = run_cases + [
    ("somefile", "Unknown"),
    ("file.py", "Code"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        result = categorize_file(input1)
    except Exception as e:
        result = f"Error: {e}"
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