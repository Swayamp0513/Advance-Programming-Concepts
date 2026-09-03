from student.details import get_student_info
from student.marks import get_gpa
from faculty.details import get_faculty_info

print(get_student_info(101, "Aakash"))
print("Student Marks Average:", get_gpa([85, 90, 80]))
print(get_faculty_info("F21", "Dr. Kulkarni", "Computer Science"))
