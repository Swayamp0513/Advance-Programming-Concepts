import pandas as pd

csv_content = """Patient_ID,Name,Age,Gender,Disease,Medical_Expense
P01,Suresh,65,M,Cardiac,75000
P02,Meena,45,F,Diabetes,32000
P03,Ramesh,72,M,Cardiac,68000
P04,Geeta,38,F,Asthma,21000
P05,Ashok,61,M,Orthopedic,54000
P06,Lata,52,F,Diabetes,46000
"""
with open("patients.csv", "w") as f:
    f.write(csv_content)

df = pd.read_csv("patients.csv")

print("Patients above 60 years:
", df[df["Age"] > 60])
print("
Average Medical Expense:", df["Medical_Expense"].mean())

top_expense_patient = df.loc[df["Medical_Expense"].idxmax()]
print("
Patient with Highest Medical Expense:
", top_expense_patient)

print("
Patient Count per Disease:
", df["Disease"].value_counts())
print("
Patients with Medical Expense > 50,000:
", df[df["Medical_Expense"] > 50000])
