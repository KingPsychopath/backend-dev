# Protecting Bank Information

You are a software developer who has been hired by a small community bank to help them automate their banking operations. The bank currently uses paper-based record-keeping and manual calculations, which makes it difficult to keep track of account balances and transactions.

## Challenge

Complete the `BankAccount` class.

### Constructor

Initialize _private_ instance variables `__account_number` to `account_number`, and `__balance` to `initial_balance`.

### Public getters

Define getter methods `get_account_number`, and `get_balance` that return the values of the private variables.

### `deposit` method

It should accept an `amount` as input and add it to the account `balance`.

### `withdraw` method

It should accept an `amount` and check if there is enough money in the account for the withdrawal.

If there are _not_ enough funds it should `raise` a [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) exception with the message `"Insufficient funds"`. Otherwise, it should deduct the `amount` from the balance.