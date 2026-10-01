import numpy as np

mat = np.arange(1, 17).reshape(4, 4)

print("Matrix:
", mat)
print("
First row:", mat[0, :])
print("Last column:", mat[:, -1])
print("Diagonal elements:", np.diag(mat))
print("Elements from second and third rows:
", mat[1:3, :])
