# Return Type = int
# Type of "n" = int
def sum_iii(n):
   total = 0
   for i in range(1, n + 1):
       total += (10 ** i - 1) // 9
   return total

print(sum_iii(3))

# range 1, n+1 because range is exclusive and we want to include n in the sum
# - also zero multiplied by itself is zero so we start from 1 to save a step

# sum_iii(3) returns 123 because 10 + 100 + 1000 = 1110
# 10 + 100 + 1000 = 1110

"""

The line of code total += (10 ** i - 1) // 9 is part of a loop that's calculating the sum of a series.

The ** operator is the exponentiation operator in Python. It raises the number on its left to the power of the number on its right. So 10 ** i is calculating 10 raised to the power of i.

The - 1 is subtracting one from the result of 10 ** i.

The // operator is the floor division operator in Python. It performs division and then rounds down (or 'floors') the result to the nearest whole number. So (10 ** i - 1) // 9 is dividing 10 ** i - 1 by 9 and rounding down the result.

The += operator is a shorthand for total = total + (10 ** i - 1) // 9. It adds the value of (10 ** i - 1) // 9 to the current value of total, and then assigns the result back to total.

So, in each iteration of the loop, this line is calculating (10 ** i - 1) // 9 and adding the result to a running total. The effect of this is to calculate the sum of the series 1, 11, 111, ..., where the number of 1's is increasing in each term of the series.




To calculate the sum of the series 2, 22, 222, ..., you can multiply the result of (10 ** i - 1) // 9 by 2. 
Here's how you can modify the line of code:

For the series 2, 22, 222, ...:

total += 2 * ((10 ** i - 1) // 9)


"""