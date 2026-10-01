import pandas as pd

csv_content = """Student_ID,Name,Department,Python,DBMS,Maths
101,Aarav,CSE,85,78,92
102,Ananya,ECE,72,68,80
103,Rohan,CSE,90,85,88
104,Isha,ME,65,70,58
105,Kavya,CSE,88,92,95
106,Tushar,IT,74,79,81
107,Pallavi,ECE,81,83,77
"""
with open("students.csv", "w") as f:
    f.write(csv_content)

df = pd.read_csv("students.csv")

print("First 5 records:
", df.head(5))
print("
Last 5 records:
", df.tail(5))

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("
Students with Total & Average Marks:
", df[["Student_ID", "Name", "Total", "Average"]])
print("
Students with Average Marks > 75:
", df[df["Average"] > 75][["Student_ID", "Name", "Average"]])

top_student = df.loc[df["Average"].idxmax()]
print("
Student with Highest Average:
", top_student[["Student_ID", "Name", "Average"]])

subject_averages = df[["Python", "DBMS", "Maths"]].mean()
print("
Average Marks for Each Subject:
", subject_averages)
