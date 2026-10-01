import pandas as pd

data = {
    "Patient ID": ["P01", "P02", "P03", "P04", "P05"],
    "Patient Name": ["Suresh", "Meena", "Ramesh", "Geeta", "Ashok"],
    "Age": [65, 45, 72, 38, 61],
    "Disease": ["Cardiac", "Diabetes", "Hypertension", "Asthma", "Orthopedic"],
    "Medical Charges": [75000, 32000, 58000, 21000, 62000]
}

df = pd.DataFrame(data)
print("Patients above 60 years:
", df[df["Age"] > 60])
print("
Average Medical Charge:", df["Medical Charges"].mean())
print("Maximum Medical Charge:", df["Medical Charges"].max())
print("
Patients with Medical Charges > 50,000:
", df[df["Medical Charges"] > 50000])
