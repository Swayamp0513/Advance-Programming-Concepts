empids  = (101, 102, 103, 104, 105)
target = 103
for id in empids:
    if id == target:
        idx = empids.index(id)
print("Index of ID", target, "is:", idx)