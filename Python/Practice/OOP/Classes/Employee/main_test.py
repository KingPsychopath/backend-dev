from main import *

run_cases = [
    ("John", "Cena", 1001, "Manager", 50000, ["John Cena", 1001, "Manager", 50000, 1]),
    (
        "Alice",
        "Wendall",
        1002,
        "Assistant Manager",
        45000,
        ["Alice Wendall", 1002, "Assistant Manager", 45000, 2],
    ),
    (
        "Emily",
        "Morcovich",
        1003,
        "Marketing Manager",
        55000,
        ["Emily Morcovich", 1003, "Marketing Manager", 55000, 3],
    ),
]

submit_cases = run_cases + [
    ("Test", "User", 1004, "Intern", 10000, ["Test User", 1004, "Intern", 10000, 4]),
    (
        "Sample",
        "User",
        1005,
        "Tech Lead",
        70000,
        ["Sample User", 1005, "Tech Lead", 70000, 5],
    ),
    (
        "Random",
        "User",
        1006,
        "Junior Developer",
        35000,
        ["Random User", 1006, "Junior Developer", 35000, 6],
    ),
    (
        "Just",
        "Another",
        1007,
        "Senior Developer",
        80000,
        ["Just Another", 1007, "Senior Developer", 80000, 7],
    ),
    ("Last", "One", 1008, "CEO", 150000, ["Last One", 1008, "CEO", 150000, 8]),
]


def test(first_name, last_name, id, position, salary, expected_output):
    print("---------------------------------")
    try:
        emp = Employee(first_name, last_name, id, position, salary)

        actual_output = [
            emp.get_name(),
            emp.id,
            emp.position,
            emp.salary,
            Employee.total_employees,
        ]

        print(f"Inputs: {first_name}, {last_name}, {id}, {position}, {salary}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {actual_output}")

        if actual_output == expected_output:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed, failed = 0, 0
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


if "__RUN__" in globals():
    test_cases = run_cases
else:
    test_cases = submit_cases

main()
