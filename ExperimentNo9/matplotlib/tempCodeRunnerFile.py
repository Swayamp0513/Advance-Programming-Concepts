
import matplotlib.pyplot as plt

students = ["Amit", "Rahul", "Priya", "Sneha", "Rohit"]
marks = [70, 85, 90, 65, 80]

plt.barh(students, marks)

plt.title("Student Marks - Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
