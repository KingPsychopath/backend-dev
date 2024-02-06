# The Calculator

# Challenge

Complete the `Calculator` class.

### Constructor

Create a _private_ instance variable called `result` initialized to `0`.

### Math

The following methods should perform their respective mathematic computations. The "left-hand side" of each operation should be the current value of the `result` variable. The "right-hand side" of each operation will be the value passed in.

- `add(self, a)`
- `subtract(self, a)`
- `multiply(self, a)`
- `divide(self, a)`: If the user attempts to divide by `0`, `raise` a `ValueError` with `"Cannot divide by zero"` as the argument
- `modulo(self, a)`: If the user attempts to divide by `0`, `raise` a `ValueError` with `"Cannot divide by zero"` as the argument
- `power(self, a)`:
- `square_root(self)`

### Helper methods

- `clear(self)`: reset the `result` variable to `0`
- `get_result(self)`: return the current value stored in the calculator's private `result` variable.