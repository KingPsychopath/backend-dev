def fibonnaci(n: int) -> int:
    # F_n  = F_n-1 + F_n-2 where F(1) = 1 and F(0) 0
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1

    return fibonnaci(n - 1) + fibonnaci(n - 2)
 # in order to find F(n), we need to find F(n-1) and F(n-2) - 
 # we do this recursively until we reach the base case
    # F(5) = F(4) + F(3)]
    # F(4) = F(3) + F(2)
    # F(3) = F(2) + F(1)
    # F(2) = F(1) + F(0)
    # F(1) = 1
    # F(0) = 0
    # F(2) = 1 + 0 = 1
    # F(3) = 1 + 1 = 2
    # F(4) = 2 + 1 = 3
    # F(5) = 3 + 2 = 5
    
    
print(fibonnaci(5))

# More efficient with tail-call recursion
def fibonnaci_tail(n: int, a: int = 0, b: int = 1) -> int:
    if (n == 0):
        return a
    elif (n == 1):
        return b

    return fibonnaci_tail(n - 1, b, a + b)

print(fibonnaci_tail(50))

# https://www.youtube.com/watch?v=_JtPhF8MshA 
# https://www.youtube.com/watch?v=-PX0BV9hGZY

# More efficient with memoization

def fibonnaci_memo(n: int, memo: dict = {}) -> int:
    if (n in memo):
        return memo[n]
    elif (n <= 0):
        return 0
    elif (n == 1):
        return 1

    memo[n] = fibonnaci_memo(n - 1, memo) + fibonnaci_memo(n - 2, memo)
    return memo[n]


# More efficient with memoization and tail-call recursion
def fibonnaci_tail_memo(n: int, a: int = 0, b: int = 1, memo: dict = {}) -> int:
    if (n == 0):
        return a
    elif (n == 1):
        return b
    elif (n in memo):
        return memo[n]

    memo[n] = fibonnaci_tail_memo(n - 1, b, a + b, memo)
    return memo[n]

# Memoization is a technique for improving the performance of recursive algorithms.
# It helps to speed up the recursive algorithm by storing the results of function calls and returning the cached result when the same inputs occur again.
# This is useful particularly in the fibonacci sequence because the recursive algorithm is very inefficient.
# It is inefficient because it calculates the same values over and over again.
# This is done when the recursive algorithm is called with the same input multiple times.
# For example, when fibonnaci(5) is called, fibonnaci(4) and fibonnaci(3) are called.
# When fibonnaci(4) is called, fibonnaci(3) and fibonnaci(2) are called.
# When fibonnaci(3) is called, fibonnaci(2) and fibonnaci(1) are called.
# When fibonnaci(2) is called, fibonnaci(1) and fibonnaci(0) are called.