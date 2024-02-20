# Filter

The built-in [filter](https://docs.python.org/3/library/functions.html#filter) function takes a function and an iterable (in this case a list), and returns a _new_ iterable that only contains elements from the original iterable where the result of the function on that item returned `True`.

```py
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```

## Assignment

Complete the `remove_invalid_lines` function. It should scan the document and _remove_ any lines that start with the old bullet point style `-`. Preserve any newline `\n` characters that were in the original document - including the newline at the very end.

```
- This is a bullet
* This is a bullet
```

Becomes:

```
* This is a bullet
```

These functions might be useful:

- [split](https://docs.python.org/3/library/stdtypes.html#str.split)
- [.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith)

_Accomplish this in a single line of code without creating any variables or using any loops!_

## Tip

Don't forget about Lambda functions!