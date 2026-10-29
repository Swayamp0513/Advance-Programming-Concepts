import pandas as pd

prices_dict = {
    "Backpack": 850,
    "Shoes": 2200,
    "Watch": 3400,
    "Water Bottle": 450,
    "Jacket": 1800
}

series = pd.Series(prices_dict)
print("All Products and Prices:
", series)

increased_prices = series * 1.10
print("
Prices after 10% increase:
", increased_prices)

print("
Most Expensive Product:", series.idxmax(), "at Rs.", series.max())
print("
Products costing more than Rs. 1,000:
", series[series > 1000])
