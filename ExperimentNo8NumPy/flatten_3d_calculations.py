import numpy as np

arr_3d = np.arange(1, 28).reshape(3, 3, 3)
flat = arr_3d.flatten()

print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print(f"Average: {np.mean(flat):.2f}")
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
