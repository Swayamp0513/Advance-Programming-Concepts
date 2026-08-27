def calculate_grade(marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return percentage, grade



marks_list = [85, 90, 78, 92, 88]
perc, gr = calculate_grade(marks_list)
print("Marks:", marks_list)
print("Percentage:", perc)
print("Grade:", gr)
