# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total_cost = 0.0

for item, quantity in cart:
    price = prices.get(item)

    if price is not None:
        item_cost = price * quantity
        total_cost += item_cost
    
    else:
        print("Brak ceny.")

print(f"Total cost: {round(total_cost, 2)}")