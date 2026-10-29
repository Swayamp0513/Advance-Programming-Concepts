import pandas as pd

data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Aarav", "Ananya", "Rohan", "Isha", "Kavya"],
    "Python Marks": [85, 72, 90, 65, 88],
    "DBMS Marks": [78, 68, 85, 70, 92],
    "Mathematics Marks": [92, 80, 88, 58, 95]
}

df = pd.DataFrame(data)
print("Student DataFrame:
", df)

df["Total Marks"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]
df["Average Marks"] = df["Total Marks"] / 3

print("
Updated DataFrame with Total & Average:
", df)

top_students = df[df["Average Marks"] > 75]
print("
Students scoring > 75% average:
", top_students[["Student ID", "Student Name", "Average Marks"]])
