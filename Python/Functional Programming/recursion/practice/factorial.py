# Descending
def factorial_descending(n):
    if n == 0:
        return 1
    
    return n * factorial_descending(n-1)

print(factorial_descending(5))

# Tail-call

def factorial(n: int, a: int = 1) -> int:
    if n == 0:
        return a
    
    return factorial(n-1, n * a)

# Flow of Code
# factorial(5, 1)
# factorial(4, 5)
# factorial(3, 20)
# factorial(2, 60)
# factorial(1, 120)
# factorial(0, 120)
# 120

print(factorial(5))
print(factorial(10))