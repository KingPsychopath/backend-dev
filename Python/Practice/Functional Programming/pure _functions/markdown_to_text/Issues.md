# No-Op

It's easy to tell that a function is impure if it doesn't return anything. If a function doesn't return anything, the only reason to call it is for its side effects.

If a pure function doesn't return anything, it's a no-op, or a [no operation](https://en.wikipedia.org/wiki/NOP_(code)), which is a fancy way of saying that it doesn't do anything, and is therefore useless.

## Useless no-op

```py
def square(x):
    x * x

# this function call makes no sense
# it's just useless computation
square(3)
```

## Useful side-effect (but impure)

```py
y = 5
def add_to_y(x):
    y += x

# this function call changes the value of y
# but it's impure, and frankly bad code
add_to_y(5)
```

## print()

The `print()` function has a side effect! It's not a pure function. It doesn't return anything, it just prints text to the console.

## Assignment

Complete the `markdown_to_text` function. It's currently a no-op.

It should:

1. Remove any `#` characters that are at the beginning of a line. ([headings](https://www.markdownguide.org/basic-syntax/#headings) in markdown)
2. Remove any `*` characters that are at the start or end of a word. ([emphasis](https://www.markdownguide.org/basic-syntax/#emphasis) in markdown)

## Tips

There is a decent amount of code in this exercise, but you can do it! Just thought I'd warn you. I used ~25 lines to write the solution.

I also wrote a separate helper function called `remove_asterisks_from_words(line)` that I used in `markdown_to_text`. You don't have to do that, but it might make your code easier to read.