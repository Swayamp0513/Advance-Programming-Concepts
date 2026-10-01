import pandas as pd

csv_content = """Employee_ID,Name,Department,Experience,Salary
1,Karan,CSE,4,65000
2,Sneha,HR,2,48000
3,Vikas,CSE,8,82000
4,Pooja,IT,3,52000
5,Aditya,ECE,6,59000
6,Megha,CSE,5,71000
"""
with open("employees.csv", "w") as f:
    f.write(csv_content)

df = pd.read_csv("employees.csv")

print("Employees from CSE Department:
", df[df["Department"] == "CSE"])
print("
Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("
Employees with Salary > 50,000:
", df[df["Salary"] > 50000])

dept_avg_salary = df.groupby("Department")["Salary"].mean()
print("
Department-Wise Average Salary:
", dept_avg_salary)
