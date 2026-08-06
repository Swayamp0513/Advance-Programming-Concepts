str = input("Enter a string: ")
upper = 0
lower = 0
for char in str:
    if char.isupper():
        upper+= 1
    elif char.islower():
        lower += 1
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
