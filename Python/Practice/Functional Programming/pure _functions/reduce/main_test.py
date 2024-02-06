from main import *

run_cases = [
    (
        ["The world is changed", "I feel it in the water", "I feel it in the earth"],
        2,
        "The world is changed. I feel it in the water.",
    ),
    (["Hello", "world", "!"], 2, "Hello. world."),
]

submit_cases = run_cases + [
    ([], 0, ""),
    (
        ["You fool of a Boots", "Throw yourself in next time"],
        2,
        "You fool of a Boots. Throw yourself in next time.",
    ),
    (
        [
            "It began with the forging of the Great Rings",
            "Three were given to the Elves, immortal, wisest and fairest of all beings",
        ],
        1,
        "It began with the forging of the Great Rings.",
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * sentences: {input1}")
    print(f" * n: {input2}")
    print(f"Expecting: {expected_output}")
    result = accumulate_first_sentences(input1, input2)
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
