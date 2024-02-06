from main import *

run_cases = [
    (
        [
            {"price": 10.00, "money_available": 125.00},
            {"price": 5.00, "money_available": 25.00},
        ],
        [115.00, 20.00],
    ),
    (
        [
            {"price": 20.01, "money_available": 20.01},
            {"price": 1.04, "money_available": 254.00},
        ],
        [0.00, 252.96],
    ),
    (
        [{"price": 99.99, "money_available": 10.00}],
        "Purchase exception: 10.00 is not enough for 99.99",
    ),
]

submit_cases = run_cases + [
    (
        [{"price": 40.20, "money_available": 6.00}],
        "Purchase exception: 6.00 is not enough for 40.20",
    ),
    (
        [
            {"price": 16.00, "money_available": 235.01},
            {"price": 10.70, "money_available": 254.10},
        ],
        [219.01, 243.40],
    ),
]


def test(purchase_orders, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * purchase_orders: {purchase_orders}")
    print(f"Expecting: {expected_output}")
    result = make_purchases(purchase_orders)
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
