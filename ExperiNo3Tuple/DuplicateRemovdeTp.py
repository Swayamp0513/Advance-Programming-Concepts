tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
merged = tuple(set(tuple1 + tuple2))
print("Merged without duplicates:", merged)