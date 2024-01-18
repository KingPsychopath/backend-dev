test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
test_tuple  = test_tuple + (11,)
print(test_tuple)

test_list_odd = [1, 2, 3, 4, 5]
test_list_even = [1, 2, 3, 4, 5, 6]

# Find middle of list
middle_odd = len(test_list_odd) // 2
middle_even = len(test_list_even) // 2
print(middle_odd)
print(middle_even)

def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(squared_nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]

a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
print(c)
print (list(c))

word_with_asterisks = '*word*'
a = word_with_asterisks[1:-1]
b = word_with_asterisks[1:]
c = word_with_asterisks[:-1]
d = '*'
if d.startswith('*') and d.endswith('*'):
    d = d[1:-1]

print(a, b, c, d)

test_string = '#'
list_of_strings = ['a', 'b', 'c']
list_of_strings.append(test_string[1:])
print(list_of_strings)
print(test_string[:])

test_list = [1]
print(test_list[1:])
print(len(test_list[1:]))

fruits = ['apple', 'banana', 'cherry']
def print_words(word):
    if len(word) == 0:
        return '/'
    
    return word[0] + ' ' + print_words(word[1:])

print(print_words(fruits))

# Pre-Oder Traversal Recursive Print
def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)

# In-Order Traversal Recursive Print
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)

# Post-Order Traversal Recursive Print
def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)

fruits = ['apple', 'banana', 'cherry']
def print_words(words, i):
    if i >= len(words):
        return
    # We call the recursive function first to print the words
    # before the current index this is called pre-order traversal
    print_words(words, i + 1)
    print(words[i])
print_words(fruits, 0)
# Output: cherry banana apple

def print_words2(words, i):
    if i >= len(words):
        return
    # We call the recursive function last to print the words
    # after the current index this is called post-order traversal
    print(words[i])
    print_words2(words, i + 1)
print_words2(fruits, 0)
# Output: apple banana cherry

def high_order_function(func: callable, n: int) -> int:
    return func(n)
