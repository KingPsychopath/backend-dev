from main import *

run_cases = [
    ("Functional programming", "gnimmargorp lanoitcnuF"),
    ("Python", "nohtyP"),
]

submit_cases = run_cases + [
    ("", ""),
    (
        "Haskell code has no side effects because no one writes it",
        "ti setirw eno on esuaceb stceffe edis on sah edoc lleksaH",
    ),
    (
        "Lisp is the #1 programming language if you measure by parentheses",
        "sesehtnerap yb erusaem uoy fi egaugnal gnimmargorp 1# eht si psiL",
    ),
    ("OCaml is for Haskell dropouts", "stuopord lleksaH rof si lmaCO"),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expected Output: {expected_output}")
    result = reverse_string(input)
    print(f"Actual Output: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Failure")
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
