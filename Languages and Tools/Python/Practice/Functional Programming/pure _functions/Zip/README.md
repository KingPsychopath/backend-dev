Reduce

The functools.reduce function is a function that takes a function and a list of values, and applies the function to each value in the list, accumulating a result as it goes.

For example:

# import the functools module
# from the standard library
import functools

def add(sum, y):
    return sum + y

numbers = [1, 2, 3, 4, 5]
sum = functools.reduce(add, numbers)
print(sum)
# 15

How do map, filter, and reduce help with FP?

Take a look at this imperative code that calculates the factorial of a number:

def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

A higher-order function like reduce will allow us to remove the stateful iteration and mutation of the result variable:

import functools

def mul(x, y):
    return x * y

def factorial(n):
    return functools.reduce(mul, range(1, n + 1))

In the functional example, we're simply composing and combining functions to get the result we want. We're doing our best to avoid keeping track of state and mutating variables.
Assignment

Complete the accumulate and the accumulate_first_sentences functions.
accumulate

This is a helper function that will be used by functools.reduce in the accumulate_first_sentences function. It should take a doc (a string representing the growing document) and a sentence (a string representing the next line to be added to the document) as input, and return a new string representing the updated document.

    If it's the first line of the document, it should return the line with no changes.
    Otherwise, it should join the sentence onto the document with a period and a space in between, resulting in correct punctuation.

accumulate_first_sentences

This function should take a list of sentences and a number of sentences to truncate to as input, and return a single string as output. The returned string should be the first n sentences of each line in the document, joined together with a period and a space in between.

Don't forget to:

    Add a period to the end of the document.
    Handle the case where the sentences list is empty by returning an empty string.

Examples

print(accumulate_first_sentences(["hello", "there", "kid"], 2))
# hello. there.

print(accumulate_first_sentences([], 0))
# (prints nothing)
