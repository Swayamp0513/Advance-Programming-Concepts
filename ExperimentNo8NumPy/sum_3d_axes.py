import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:
", arr)
print("
Sum of all elements:", np.sum(arr))
print("Sum of each layer (along axis 0):
", np.sum(arr, axis=(1, 2)))
print("Sum along rows (along axis 1):
", np.sum(arr, axis=1))
print("Sum along columns (along axis 2):
", np.sum(arr, axis=2))
