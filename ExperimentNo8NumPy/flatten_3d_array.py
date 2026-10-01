import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)
flattened = arr_3d.flatten()

print("Original 3D Array:
", arr_3d)
print("
Flattened 1D Array:
", flattened)
