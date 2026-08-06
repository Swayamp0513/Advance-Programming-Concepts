str = input("Enter a string: ")
target = input("Enter character: ")
frequency = 0
for char in str:
    if char == target:
        frequency += 1
print(f"The character '{target}' appears {frequency} times.")
