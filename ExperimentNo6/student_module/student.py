def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    return 'F'
