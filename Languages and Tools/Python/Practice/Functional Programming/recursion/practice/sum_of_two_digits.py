# 3. Write a recursive function that accepts a number as its argument and returns the sum of digits.
# Did it with left-hand priority and passed on the digits on the right-hand side of the decimal point in the number to the next recursive call.
def sum_of_digits(a):
    if a == 0:
        return a
    
    return a // (10 ** (len(str(a)) - 1)) + sum_of_digits(a % (10 ** (len(str(a)) - 1)))

print(sum_of_digits(123))

def sum_of_digits_tidy(a):
    if a == 0:
        return a
    
    divisor = 10 ** (len(str(a)) - 1)
    return a // divisor + sum_of_digits_tidy(a % divisor)

print(sum_of_digits_tidy(123))
print(sum_of_digits_tidy(23456))

# Now I'll do it by passing the digits on the left hand side of the decimal place to the next recursive call.
def sum_digits_left(a):
    if a < 10:
        return a
    
    return a % 10 + sum_digits_left(a // 10)

print(sum_digits_left(123))
print(sum_digits_left(23456))