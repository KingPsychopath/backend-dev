## Assignment

Complete the `accumulate` and the `accumulate_first_sentences` functions.

### accumulate

This is a helper function that will be used by [functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce) in the `accumulate_first_sentences` function. It should take a `doc` (a string representing the growing document) and a `sentence` (a string representing the next line to be added to the document) as input, and return a new string representing the updated document.

- If it's the first line of the document, it should return the line with no changes.
- Otherwise, it should join the sentence onto the document with a period and a space in between, resulting in correct punctuation.

### accumulate_first_sentences

This function should take a list of sentences and a number of sentences to truncate to as input, and return a single string as output. The returned string should be the first `n` sentences of each line in the document, joined together with a period and a space in between.

Don't forget to:

- Add a period to the end of the document.
- Handle the case where the `sentences` list is empty by returning an empty string.

### Examples

```py
print(accumulate_first_sentences(["hello", "there", "kid"], 2))
# hello. there.
```

```py
print(accumulate_first_sentences([], 0))
# (prints nothing)
```