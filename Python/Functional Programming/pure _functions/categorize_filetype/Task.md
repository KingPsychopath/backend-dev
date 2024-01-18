# Anonymous Functions

Anonymous functions are true to form in that they have _no name_. In Python, we call these _lambda functions_ after [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus).

```py
lambda x: x + 1
```

This is a function that takes in a single argument `x` and returns the result of `x + 1`. We can assign this function to a variable and call it like any other function.

```py
add_one = lambda x: x + 1

print(add_one(2))
# 3
```

This allows us to create functions on the fly and pass them around as data! It's _functions as values._

## Assignment

Complete the `categorize_file` function. It takes a single string argument, `filename`, and should return a string representing the category of the file. The categories are as follows:

- `Text` if the file ends with `.txt`
- `Document` if the file ends with `.docx`
- `Code` if the file ends with `.py`
- `Unknown` if the file ends with anything else

The last line of the function is already written for you. It does the heavy lifting of parsing the extension out of the filename. You just need to write the logic for determining the category.

The last line expects an anonymous `get_category` function to exist. You should create that function using a lambda expression. It should take in a single argument, `extension`, and return a string representing the category of the file.

## Tip

I used the built-in dictionaries [.get](https://docs.python.org/3/library/stdtypes.html#dict.get) method to implement this.

```py
person = {
  'name': 'Alice',
  'age': 30,
  'city': 'New York'
}

age = person.get('age')
print(f"The person's age is: {age}")
# Prints: The person's age is 30
```