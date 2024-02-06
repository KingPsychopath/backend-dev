# It's Math

Functional programming tends to be popular amongst developers with a strong mathematical background.

![confused math](https://i.imgur.com/YI3kwUq.png)

After all, a math equation isn't procedural: it's declarative. For example, take the following math equation:

```
avg = Σx/N
```

It might look scary, but this symbol, `Σ`, is just the big Greek letter [Sigma](https://en.wikipedia.org/wiki/Sigma). It's used to represent a [sum](https://en.wikipedia.org/wiki/Summation). `Σx` just represents the sum of all the numbers in a list `x`. Next, to calculate an average, we divide by `N`, the number of elements in the list.

This math equation is a _declarative_ way of writing "the average of the numbers".

If we want to write some _code_ from scratch that does the same thing, it might look like this in a procedural (imperative) paradigm:

```py
def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

However, with functional programming, we can write code that looks like this:

```py
def get_average(nums):
    return sum(nums) / len(nums)
```

Here we're not keeping track of any state (the `total` variable). We're simply composing functions together to get the result we want. _We're doing our best to avoid keeping track of state (mutating variables)_

## Assignment

In the world of document conversion, you'll sometimes need to handle fonts and font sizes. Complete the `get_median_font_size` function.

Given a list of numbers representing font sizes, return the [median](https://en.wikipedia.org/wiki/Median) font size. If the list is empty, return `None`. If the list has an even number of elements, return the average of the two middle elements.

> Median: the middle number in a sorted list of numbers. If there are an even number of numbers, return the average of the two middle numbers.

You will probably want to:

- Use the [sorted](https://docs.python.org/3/library/functions.html#sorted) function
- Use the [len](https://docs.python.org/3/library/functions.html#len) function
- Take advantage of [list slicing](https://www.learnbyexample.org/python-list-slicing/) to get the middle elements
- Use the [floor division](https://docs.python.org/3/glossary.html#term-floor-division) operator `//` to get the index of the middle element

Be sure to use a functional paradigm! Your code should:

1. Not use any loops
2. Not mutate any variables (it's okay to create new ones, though)