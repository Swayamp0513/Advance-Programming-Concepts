import pandas as pd

data = {
    "Order_ID": [501, 502, 503, 504, 505],
    "Customer": ["John", "Sara", "Michael", "Emma", "David"],
    "Product": ["Laptop", "Mouse", "Desk", "Chair", "Speaker"],
    "Quantity": [1, 5, 2, 4, 3],
    "Price": [55000, 600, 4000, 2500, 1800],
    "Discount": [3000, 100, 500, 400, 200]
}

df = pd.DataFrame(data)
df["Final Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:
", df)
print("
Orders Above Rs. 5,000:
", df[df["Final Amount"] > 5000])

highest_order = df.loc[df["Final Amount"].idxmax()]
print("
Highest-Value Order:
", highest_order)
print("
Average Order Value:", df["Final Amount"].mean())
