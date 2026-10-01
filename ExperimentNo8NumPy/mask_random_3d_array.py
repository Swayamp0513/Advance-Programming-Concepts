import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Random 3D Array:
", arr)
arr[arr > 50] = 0
print("
Array after replacing elements > 50 with 0:
", arr)
