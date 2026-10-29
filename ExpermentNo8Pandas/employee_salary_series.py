import pandas as pd

salaries_dict = {
    "Manish": 48000,
    "Pankaj": 62000,
    "Sunita": 53000,
    "Tanvi": 39000,
    "Varun": 75000
}

series = pd.Series(salaries_dict)
print("Employee Salary Series:
", series)
print("
Highest Salary:", series.max())
print("Lowest Salary:", series.min())
print("Average Salary:", series.mean())
print("
Employees earning > Rs. 50,000:
", series[series > 50000])
