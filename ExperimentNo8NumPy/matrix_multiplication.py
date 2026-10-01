import numpy as np

mat1 = np.array([[1, 2], [3, 4], [5, 6]])
mat2 = np.array([[7, 8, 9], [10, 11, 12]])

product = np.matmul(mat1, mat2)

print("Matrix 1 (3x2):
", mat1)
print("Matrix 2 (2x3):
", mat2)
print("Matrix Product (3x3):
", product)
