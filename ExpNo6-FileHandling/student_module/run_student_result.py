import student

marks = [85, 78, 92, 88, 74]
tot = student.calculate_total(marks)
perc = student.calculate_percentage(marks)
grd = student.calculate_grade(perc)

print("Total Marks:", tot)
print(f"Percentage: {perc:.2f}%")
print("Grade:", grd)
