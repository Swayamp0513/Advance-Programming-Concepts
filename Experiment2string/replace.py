string = input("Enter a string: ")
target = input("Enter character to replace: ")
replace = input("Enter new character: ")
result = ""
for char in string:
    if char == target:
        result += replace
    else:
        result += char
print(f"Modified string: {result}")
