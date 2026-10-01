import numpy as np

np.random.seed(10)
arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
avg = np.mean(flat)

print("Flattened Array:
", flat)
print("
Elements > 50:
", flat[flat > 50])
print("
Even elements:
", flat[flat % 2 == 0])
print(f"
Average value: {avg:.2f}")
print("Elements less than average:
", flat[flat < avg])
