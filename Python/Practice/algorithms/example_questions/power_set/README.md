
# Order 2^N - Exponential

`O(2^n)` is the first Big O class that we've dealt with that falls into the scary _exponential_ category of algorithms.

Algorithms that grow at an exponential rate become impossible to compute after so few iterations that they are almost worthless in practicality.

## Assignment

At Socialytics we need to be able to compute the [power set](https://en.wikipedia.org/wiki/Power_set) of a set of influencers. Something about targeting segments of an audience with ads. I don't know, I just do what I'm told.

A power set is the set of all possible subsets of a set. For example, the set `{1, 2, 3}` has the power set:

`{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}`.

_We'll work with lists instead of sets for simplicity._

Complete the `power_set` function using the following algorithm:

1. Check if the input list is empty. If it is, return a list containing an empty list. (The power set of an empty set is a set containing just the empty set)
2. Otherwise, create an empty list to hold all the final subsets of the input list.
3. Recursively call `power_set`. Pass in all of the elements in the input set _except the first one_.
4. Iterate over the list of subsets returned from the recursive call. For each subset, append two new subsets to the _final_ list of subsets:
    1. first_item_from_input_set + subset
    2. subset
5. Return the list of subsets

## Observe!

Notice how the `power_set()` function gets _exponentially_ slower with each iteration, this is because its complexity class is `O(2^n)`

You couldn't complete `power_set()` with an input of just 22 items on modern hardware, even if you had a million years!