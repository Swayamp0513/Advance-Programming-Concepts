import pandas as pd

attendance_dict = {
    "Arjun": 72.5,
    "Deepika": 94.0,
    "Farhan": 68.0,
    "Gauri": 88.5,
    "Harsh": 91.0
}

series = pd.Series(attendance_dict)
print("Attendance Series:
", series)
print("
Average Attendance:", series.mean())
print("
Students with attendance below 75%:
", series[series < 75])
print("
Students with attendance above 90%:
", series[series > 90])
print("
Highest Attendance:", series.idxmax(), "with", series.max(), "%")
