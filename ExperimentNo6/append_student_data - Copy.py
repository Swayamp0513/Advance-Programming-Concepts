name = input("Enter new student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
sem = input("Enter semester: ")

with open("student.txt", "a") as f:
    f.write(f"Name: {name}\nRoll No: {roll}\nBranch: {branch}\nSemester: {sem}\n")

print("Record appended successfully to student.txt")
