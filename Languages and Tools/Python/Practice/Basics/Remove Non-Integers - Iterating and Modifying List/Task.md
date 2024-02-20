# Remove Numbers

Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.
```python 
remove_nonints(['1', 1, '3', '400', 4, 500])
# Remaining list after removing nonints = [1, 4, 500]
```

You can check the type of a variable using type() function

if type(variable) == int:

Do not change the input nums list, return a new list with the non-integers removed.


Error Convo:

Your function is skipping elements because you're modifying the list as you're iterating over it, which can lead to unpredictable results. When you remove an item from a list during a loop, the index of subsequent items changes, which means some items get skipped. Do you have an idea how you might avoid this issue?

# List Comprehension

Another way you could approach this is by using list comprehension. This technique allows you to create a new list based on an existing one. By applying a condition inside the list comprehension, you can filter out the elements you don't want.

Would you like to give it a shot? Remember in list comprehension, it goes something like [expression for item in list if condition]. Can you form that for your function?

# Slicing
By saying nums[:], you are essentially making a copy of the entire nums list. The : operator slices the list from the start to the end if you don't provide any indices.

So when you write for i in nums[:], you're creating a loop over each element in a copy of the nums list. This allows you to modify the original list nums without any skipping elements as we have experienced before.

Do you understand the difference and why you might choose to use a list slice nums[:] or a list comprehension in different scenarios?
