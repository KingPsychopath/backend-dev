# Return Type = int
# Type of "n" = int
def sum_i(n):
    sum = 0

    for i in range(1, n + 1): 
        sum += 10**i

    return sum

# range n+1 because range is exclusive and we want to include n in the sum
# - also zero multiplied by itself is zero so we start from 1 to save a step
# sum_i(3) returns 1110 because 10 + 100 + 1000 = 1110


"""
Find sum of the series 10 + 100 + 1000 + ... + 10^n

Example 1:
Input: n = 2
Output: 110
Explanation: Because 10 + 100 = 110

"""