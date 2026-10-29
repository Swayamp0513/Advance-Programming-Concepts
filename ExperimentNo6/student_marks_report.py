data = """RollNo,Name,Marks
101,Amit,85
102,Priya,92
103,Rahul,78
"""
with open("students_records.csv", "w") as f:
    f.write(data)

records = []
with open("students_records.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        parts = line.strip().split(",")
        records.append((parts[0], parts[1], float(parts[2])))

print("All Records:")
for r in records:
    print(f"Roll: {r[0]}, Name: {r[1]}, Marks: {r[2]}")

highest = max(records, key=lambda x: x[2])
avg_marks = sum(r[2] for r in records) / len(records)

print("\nHighest Scorer:", highest[1], "with marks", highest[2])
print("Class Average Marks:", round(avg_marks, 2))

print("\nStudents with Marks > 80:")
for r in records:
    if r[2] > 80 :
        print(f"{r[1]} ({r[2]})")