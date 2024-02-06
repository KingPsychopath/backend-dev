# 4. Write a program that reads two integers from keyboard and calculate the greatest common divisor (gcd) using recursive function. Solution

# This uses Euclidiean's Algorithm - I did not know this mathematical algorithm prior
def gcd(a, b):
    if b > a:
        a, b = b, a
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
    
print(gcd(60, 455))

'''
455 % 60 = 35
(60, 35)
60 % 35 = 25
(35,  25)
35 % 25 = 10
(35, 10)
35 % 10 = 5
(10, 5)
10 % 5 = 0
(5, 0)

For any number n, the GCD of n and 0 is n itself.
'''

'''
The GCD of two integers is the largest number that divides both of them without leaving a remainder.

For any number n, the GCD of n and 0 is n itself.

For any two numbers a and b, if b is not 0, the GCD can be found using the Euclidean algorithm, which is based on the principle that the GCD of a and b is the same as the GCD of b and a % b.

So, every pair of integers, regardless of whether they are positive, negative, or zero, has a GCD.
'''