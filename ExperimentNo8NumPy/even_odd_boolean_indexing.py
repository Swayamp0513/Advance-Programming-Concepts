import numpy as np

arr = np.arange(1, 21)
evens = arr[arr % 2 == 0]
odds = arr[arr % 2 != 0]

print("Original Array:", arr)
print("Even numbers:", evens)
print("Odd numbers:", odds)
