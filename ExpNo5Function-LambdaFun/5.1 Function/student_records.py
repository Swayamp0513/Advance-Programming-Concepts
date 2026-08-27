def get_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'



def process_student(student):
    total = sum(student['marks'])
    percentage = total / 5
    grade = get_grade(percentage)
    return total, percentage, grade

def process_class(students):
    class_total = 0
    highest = None
    lowest = None
    max_marks = -1
    min_marks = 501
    
    for s in students:
        total, perc, grade = process_student(s)
        class_total += total
        if total > max_marks:
            max_marks = total
            highest = s['name']
        if total < min_marks:
            min_marks = total
            lowest = s['name']
            
    avg_marks = class_total / len(students)
    return avg_marks, highest, lowest

student_list = [
    {'name': 'Alice', 'roll': 101, 'marks': [80, 85, 90, 75, 88]},
    {'name': 'Bob', 'roll': 102, 'marks': [60, 65, 70, 55, 58]},
    {'name': 'Charlie', 'roll': 103, 'marks': [95, 92, 98, 90, 94]}
]
avg, top, bot = process_class(student_list)
print(f"Class Avg Marks: {avg}, Top Scorer: {top}, Lowest Scorer: {bot}")
