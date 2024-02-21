# Newton's Method for Square Roots in Go

## Problem

The problem is to calculate the square root of a given number using Newton's method (also known as the Babylonian method).

## Intuition

Newton's method is an iterative method for finding successively better approximations to the roots (or zeroes) of a real-valued function. The process starts with an initial guess and then uses the derivative of the function to refine the guess until it is close enough to the actual root.

## Approach

The approach taken in this code is to implement Newton's method in a Go function. The function takes a number as input and returns the square root of that number. The square root is calculated by starting with an initial guess and then repeatedly applying a formula to get a better guess.

The formula used is:

```go
betterGuess := (guess + n/guess) / 2.0
```

In the context of the `Sqrt` function, which is implementing the Newton's method for calculating square roots:

- `guess` represents the current approximation of the square root of `n`. It's the value that the function is iteratively trying to improve.

- `n / guess` is part of the formula used to generate a better approximation of the square root. If `guess` is an overestimate of the square root of `n`, then `n / guess` will be an underestimate, and vice versa. Averaging `guess` and `n / guess` gives a better approximation of the square root.

The `delta` variable represents the precision of the result. The loop continues until the difference between the current guess and the previous guess is less than delta.

## Complexity Analysis

The time complexity for this approach is O(log n) because the number of iterations required to get a good approximation of the square root is logarithmic in the input number.

## References

https://www.youtube.com/watch?v=FpOEx6zFf1o
