import pandas as pd

csv_content = """Date,City,Temperature,Humidity,Rainfall
2026-06-01,Mumbai,34.5,80,12.0
2026-06-01,Delhi,38.2,55,0.0
2026-06-01,Pune,31.0,65,4.5
2026-06-02,Mumbai,33.0,82,15.2
2026-06-02,Delhi,39.5,50,0.0
2026-06-02,Pune,36.1,60,2.1
"""
with open("weather.csv", "w") as f:
    f.write(csv_content)

df = pd.read_csv("weather.csv")

print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())
print(f"Average Temperature: {df['Temperature'].mean():.2f}")
print("
Records where Temperature > 35°C:
", df[df["Temperature"] > 35])

city_avg_temp = df.groupby("City")["Temperature"].mean()
print("
City-Wise Average Temperature:
", city_avg_temp)
