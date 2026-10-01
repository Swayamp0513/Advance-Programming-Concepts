import numpy as np

np.random.seed(0)
arr = np.random.randint(1, 100, size=(3, 4, 5))

print("3D Array shape:", arr.shape)
print(f"Mean: {np.mean(arr):.2f}")
print(f"Median: {np.median(arr):.2f}")
print(f"Standard Deviation: {np.std(arr):.2f}")
print(f"Variance: {np.var(arr):.2f}")
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
