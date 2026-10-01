import pandas as pd

data = {
    "Employee ID": [1, 2, 3, 4, 5],
    "Employee Name": ["Amit", "Sneha", "Vikram", "Pooja", "Rajesh"],
    "Department": ["IT", "HR", "Finance", "IT", "Operations"],
    "Salary": [55000, 48000, 72000, 51000, 64000],
    "Experience": [4, 2, 8, 3, 6]
}

df = pd.DataFrame(data)
print("Employees with Salary > 50,000:
", df[df["Salary"] > 50000])

print("
Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

highest_exp_emp = df.loc[df["Experience"].idxmax()]
print("
Employee with Highest Experience:
", highest_exp_emp)
