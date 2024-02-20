# Map

"Map", "filter", and "reduce" are three functions that are commonly used in functional programming. They are also the names of three of the most common [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function) in functional programming languages.

In Python, the built-in [map](https://docs.python.org/3/library/functions.html#map) function takes a function and an [iterable](https://docs.python.org/3/glossary.html#term-iterable) (in this case a list), and returns a _new_ iterable where the function has been applied to each element of the original iterable. This allows us to compose functions that operate on entire lists without having to write a loop and store state in variables. For example:

```py
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]
```

## Assignment

Markdown supports two different styles of bullet points, `-` and `*`. We need a function that will convert any `-` bullet points in a document to `*` bullet points.

Complete the `change_bullet_style` function. It should take a document (string) as input, and return a single string as output. The returned string should have any lines that start with a `-` character replaced with a `*` character. Preserve any newline `\n` characters that were in the original document.

For example:

```
- This is a bullet
- This is a bullet
```

Becomes:

```
* This is a bullet
* This is a bullet
```

Use the built-in [map](https://docs.python.org/3/library/functions.html#map) function to apply the pre-built `convert_line` function to each line of the input string.

These functions will also be useful for splitting and joining the whole document:

- [.split()](https://docs.python.org/3/library/stdtypes.html#str.split)
- [.join()](https://docs.python.org/3/library/stdtypes.html#str.join)

Don't forget you can use the `.join` function on a newline `"\n"`.

_Accomplish this in a single line of code without creating any variables or using any loops!_