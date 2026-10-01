import pandas as pd

marks_dict = {
    "Aditya": 82,
    "Bhavna": 68,
    "Chetan": 91,
    "Divya": 74,
    "Esha": 85
}

series = pd.Series(marks_dict)
print("Student Marks Series:
", series)
print("
Marks of Chetan:", series["Chetan"])
print("Maximum Marks:", series.max())
print("Minimum Marks:", series.min())
print("Average Marks:", series.mean())
print("
Students who scored > 75:
", series[series > 75])
