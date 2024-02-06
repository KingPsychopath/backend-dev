def factorial(num):
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial

def factorial_recursive(num):
    if num == 0:
        return 1
    return num * factorial_recursive(num - 1)
