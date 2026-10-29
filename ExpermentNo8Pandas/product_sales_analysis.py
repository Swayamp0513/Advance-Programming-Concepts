import pandas as pd

data = {
    "Product ID": [1001, 1002, 1003, 1004, 1005],
    "Product Name": ["Keyboard", "Mouse", "Monitor", "Headphones", "Webcam"],
    "Category": ["Electronics", "Electronics", "Electronics", "Audio", "Video"],
    "Price": [1200, 500, 8500, 2000, 2500],
    "Quantity": [10, 25, 4, 15, 8]
}

df = pd.DataFrame(data)
df["Total Amount"] = df["Price"] * df["Quantity"]
print("Products DataFrame:
", df)

top_product = df.loc[df["Total Amount"].idxmax()]
print("
Product with Highest Total Sales:
", top_product)
