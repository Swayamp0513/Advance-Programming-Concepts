import numpy as np

mat = np.arange(1, 17).reshape(4, 4)

print("Matrix:
", mat)
print("Sum of each row (horizontal):", np.sum(mat, axis=1))
print("Sum of each column (vertical):", np.sum(mat, axis=0))
