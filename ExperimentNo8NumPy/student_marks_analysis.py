import numpy as np

marks = np.array([78, 85, 92, 64, 89, 73, 95, 81, 70, 88])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print(f"Standard Deviation: {np.std(marks):.2f}")
