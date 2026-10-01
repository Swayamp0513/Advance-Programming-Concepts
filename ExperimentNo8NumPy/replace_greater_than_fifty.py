import numpy as np

arr = np.array([15, 62, 34, 88, 45, 91, 23, 76, 50, 12])

print("Original array:", arr)
arr[arr > 50] = 0
print("Modified array (elements > 50 replaced with 0):", arr)
