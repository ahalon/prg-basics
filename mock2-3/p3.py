def f(inventory):
    min_diff = -1
    max_product = None
    for product, price in inventory.items():
        diff = max(price) - min(price)
        if diff > min_diff:
            min_diff = diff
            max_product = product
    return max_product
