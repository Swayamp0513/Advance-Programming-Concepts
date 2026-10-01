import numpy as np

arr = np.array([45, 12, 89, 23, 67, 34, 90, 11])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Unsorted array:", arr)
print("Ascending order:", ascending)
print("Descending order:", descending)
