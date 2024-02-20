def make_purchases(purchase_orders):
    money_left_in_each_account = []

    for purchase_order in purchase_orders:
        try:
            leftovers = purchase(purchase_order['price'], purchase_order['money_available'])
            money_left_in_each_account.append(leftovers)
        except Exception as e:
            return f'Purchase exception: {e}'


    return money_left_in_each_account


# Don't edit below this line


def purchase(price, money_available):
    if money_available < price:
        raise Exception(f"{money_available:.2f} is not enough for {price:.2f}")
    return money_available - price
