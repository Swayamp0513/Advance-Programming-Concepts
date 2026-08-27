list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, list1, list2))
print("List 1:", list1)
print("List 2:", list2)
print("Sum of corresponding elements:", sums)
