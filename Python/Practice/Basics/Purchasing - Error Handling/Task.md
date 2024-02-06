
# Purchasing

Now we need to use our `purchase` function to process an entire list of purchase orders.

## Challenge

Complete the `make_purchases` function. It accepts a list of dictionaries representing purchase orders. You can take a look at the test suite for an example of the shape of the data.

It returns a list of floats representing the amount of money left in each customer's account after completing a purchase. The returned list may be smaller because it will only contain the leftover amounts of the customers who were able to successfully complete a purchase.

`make_purchases()` should create an empty list of "leftovers", and then loop over each order, running the `purchase()` function for each one. If an exception is raised, return the string:

```
Purchase exception: ERROR
```

_Where `ERROR` is the exception's text._

Then continue to the next order without adding anything to the leftovers list.

Otherwise, if the purchase was successful, append the leftover amount to the "leftovers" list.

At the end of the loop return the leftovers list.

_The order of the returned list should be the same as the input, but with the invalid items removed._