import pandas as pd

data = {
    "Product_ID": [301, 302, 303, 304, 305],
    "Product_Name": ["Printer", "USB Drive", "Smartwatch", "Hard Disk", "Tablet"],
    "Category": ["Hardware", "Accessories", "Wearables", "Storage", "Electronics"],
    "Price": [9500, 650, 3200, 4500, 16000],
    "Quantity": [2, 10, 4, 3, 1]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Retail Sales DataFrame:
", df)
print("
Products with sales > Rs. 10,000:
", df[df["Total_Sales"] > 10000])

max_sale_product = df.loc[df["Total_Sales"].idxmax()]
print("
Product with Maximum Sales:
", max_sale_product)
print("
Average Sales:", df["Total_Sales"].mean())
