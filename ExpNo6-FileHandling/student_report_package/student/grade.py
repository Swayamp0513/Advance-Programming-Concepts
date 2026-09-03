def compute_grade(percentage):
    if percentage >= 85: return "Distinction"
    if percentage >= 60: return "First Class"
    if percentage >= 40: return "Pass"
    return "Fail"
