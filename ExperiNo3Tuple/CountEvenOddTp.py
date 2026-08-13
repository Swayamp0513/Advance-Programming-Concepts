numbers = (12, 7, 19, 24, 30, 5, 8, 11, 14, 22, 3, 16, 9, 2, 21)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even+= 1
    else:
        odd+= 1
print("Even numbers:", even)
print("Odd numbers:", odd)