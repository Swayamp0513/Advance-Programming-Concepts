import pandas as pd

data = {
    "Student_ID": [201, 202, 203, 204, 205],
    "Name": ["Nitin", "Priya", "Rahul", "Swati", "Karan"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ME"],
    "Total_Classes": [60, 60, 60, 60, 60],
    "Classes_Attended": [42, 55, 38, 50, 35]
}

df = pd.DataFrame(data)
df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Attendance Records:
", df)
print("
Students with attendance below 75%:
", df[df["Attendance Percentage"] < 75])
