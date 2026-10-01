import pandas as pd

ages_dict = {
    "PT101": 45,
    "PT102": 68,
    "PT103": 74,
    "PT104": 29,
    "PT105": 62
}

series = pd.Series(ages_dict)
print("Patient Ages Series:
", series)
print("
Average Age:", series.mean())
print("Oldest Patient:", series.idxmax(), "with age", series.max())
print("Youngest Patient:", series.idxmin(), "with age", series.min())
print("
Patients above 60 years:
", series[series > 60])
