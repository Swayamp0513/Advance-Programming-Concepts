numbers = (1, 2, 3, 2, 4, 2, 5,5,7,2)
t = 2
count =0
for n in numbers:
    if n == t:
        count += 1
print("The number", t, "appears", count, "times.")