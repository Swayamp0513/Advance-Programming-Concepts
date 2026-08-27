def calculate_total_bill(prices, quantities, discount_percent):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    discount = (total * discount_percent) / 100
    return total - discount
item_prices = [100, 250, 50]
item_qty = [2, 1, 4]
disc = 10
print("Final Bill Amount:", calculate_total_bill(item_prices, item_qty, disc))
