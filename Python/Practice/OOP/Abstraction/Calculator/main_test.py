from main import *

run_cases = [
    (10, [("add", 5), ("subtract", 3)], 12),
    (5, [("multiply", 2), ("divide", 2)], 5),
]

submit_cases = run_cases + [
    (10, [("divide", 0)], "Cannot divide by zero"),
    (7, [("modulo", 4)], 3),
    (10, [("power", 2), ("clear", None)], 0),
    (10, [("square_root", None), ("add", 5)], 8.16227766016838),
]

actions = {
    "add": Calculator.add,
    "subtract": Calculator.subtract,
    "multiply": Calculator.multiply,
    "divide": Calculator.divide,
    "modulo": Calculator.modulo,
    "power": Calculator.power,
    "square_root": Calculator.square_root,
    "clear": Calculator.clear,
}


def test(starting_num, actions_list, expected_output):
    print("---------------------------------")
    print(f"Starting Number: {starting_num}, Actions: {actions_list}")
    print(f"Expected Output: {expected_output}")
    calculator = Calculator()
    calculator.add(starting_num)
    try:
        for action, number in actions_list:
            if number is None:
                actions[action](calculator)
            else:
                actions[action](calculator, number)
        result = calculator.get_result()
        print(f"Actual Output: {result}")
        if float(result) == float(expected_output):
            print("Pass 2")
            return True
        else:
            print("Fail 1")
            return False
    except Exception as e:
        result = str(e)
        print(f"Actual output: {result}")
    if result == expected_output:
        print("Pass 1")
        return True
    else:
        print("Fail 2")
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
