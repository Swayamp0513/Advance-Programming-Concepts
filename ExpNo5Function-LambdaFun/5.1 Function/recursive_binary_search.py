def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)




arr = [10, 20, 30, 40, 50, 60]
target = 40
res = binary_search(arr, target, 0, len(arr) - 1)
print(f"Element {target} found at index:", res)
