import numpy as np

marks = np.array([55, 78, 82, 90, 65, 72, 88, 94, 60, 73,
                  81, 69, 75, 85, 92, 58, 64, 77, 89, 91])

avg = np.mean(marks)
above_avg = marks[marks > avg]

print("All Marks:", marks)
print(f"Class Average: {avg:.2f}")
print("Marks above average:", above_avg)
