def getMinTransactions(n, debts):
    # Create a balance array
    balance = [0]*n
    for debt in debts:
        from_i, to_i, amount = debt
        balance[from_i] -= amount
        balance[to_i] += amount

    # Filter out people with zero balance
    balance = [amt for amt in balance if amt != 0]

    # Use DFS to find the minimum number of transactions
    def dfs(s):
        while s < len(balance) and balance[s] == 0:
            s += 1
        if s == len(balance):
            return 0
        min_transactions = float('inf')
        for i in range(s+1, len(balance)):
            if balance[s] * balance[i] < 0:  # one is debtor, the other is creditor
                # settle s with i
                balance[i] += balance[s]
                min_transactions = min(min_transactions, 1 + dfs(s+1))
                # backtrack
                balance[i] -= balance[s]
        return min_transactions

    return dfs(0)

# Test the function
n = 3
debts = [[0, 1, 20], [1, 0, 5], [1, 2, 10], [2, 0, 10]]
print(getMinTransactions(n, debts))  # Expected output: 1

def test_getMinTransactions():
    n = 3
    debts = [[0, 1, 10], [2, 0, 5]]
    assert getMinTransactions(n, debts) == 2

print(test_getMinTransactions()