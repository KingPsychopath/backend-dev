# Return Type = int
# Type of "n" = int
def sum_ii(n):
   total = 0
   for i in range(1, n + 1):
       total += 10 ** i - 1
   return total

print(sum_ii(3))

# range 1, n+1 because range is exclusive and we want to include n in the sum
# - also zero multiplied by itself is zero so we start from 1 to save a step
# sum_ii(3) returns 1110 because 10 + 100 + 1000 = 1110

