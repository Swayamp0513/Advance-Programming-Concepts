from student.marks import get_total, get_percentage
from student.grade import compute_grade
from student.attendance import check_eligibility

marks = [88, 79, 91, 84, 76]
total = get_total(marks)
perc = get_percentage(marks)
grade = compute_grade(perc)
eligible, att_perc = check_eligibility(42, 50)

print(f"Total: {total}, Percentage: {perc:.2f}%, Grade: {grade}")
print(f"Attendance: {att_perc}%, Exam Eligible: {eligible}")
