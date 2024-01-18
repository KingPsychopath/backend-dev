"""
Our job is to build a fence that has n fences but n + 1 post. Print the following pattern: |==|==| ... |==|

Example 1:
Input: n = 2
Print Output: |==|==|
Example 2:
Input: n = 3
Print Output: |==|==|==|

"""

# Type of "n" = int
def fence_post_ii2(n):
    if n > 0:
        print('|', end='')
    
    print('==|' * n)


# Type of "n" = int
# The function fence_post_ii takes an integer n as an argument.
def fence_post_ii(n):
    # The string '==|' is repeated n times and then enclosed between '|'.
    # This forms the fence string.
    fence = '|{}'.format('==|' * n)
    # The fence string is printed.
    print(fence)

fence_post_ii(4)