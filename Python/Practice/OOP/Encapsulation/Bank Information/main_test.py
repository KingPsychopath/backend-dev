from main import *

run_cases = [
    ("1234567890", 100.0, 50.0, 75.0, 75.0),
    ("0987654321", 500.0, 100.0, 200.0, 400.0),
]

submit_cases = run_cases + [
    ("1234567890", 100.0, 50.0, 200.0, 150.0, "Insufficient funds"),
    ("0987654321", 500.0, 500.0, 500.0, 500.0),
    ("1234567890", 100.0, 0.0, 0.0, 100.0),
    ("0987654321", 500.0, 0.0, 500.0, 0.0),
]


def test(
    account_number,
    initial_balance,
    deposit_amount,
    withdraw_amount,
    expected_balance,
    error=None,
):
    print("---------------------------------")
    try:
        print(
            f"Inputs: account_number: {account_number}, initial_balance: {initial_balance:.2f}, deposit_amount: {deposit_amount:.2f}, withdraw_amount: {withdraw_amount:.2f}"
        )
        account = BankAccount(account_number, initial_balance)
        account.deposit(deposit_amount)

        try:
            account.withdraw(withdraw_amount)
            if error:
                print(f'Expected output "{error}"')
                print(f"Actual output: No error was raised")
                print("Fail")
                return False
            if account.get_balance() == expected_balance:
                print(f"Expected balance ${expected_balance:.2f}")
                print(f"Actual balance ${account.get_balance():.2f}")
                print("Pass")
                return True
            else:
                print(f"Expected balance ${expected_balance:.2f}")
                print(f"Actual balance ${account.get_balance():.2f}")
                print("Fail")
                return False
        except ValueError as e:
            if str(e) == error:
                print(f'Expected error "{error}"')
                print(f'Actual error "{e}"')
                print("Pass")
                return True
            else:
                print(f'Expected error "{error}"')
                print(f'Actual output "{e}"')
                return False
    except Exception as e:
        print(f"Fail: {e}")
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
