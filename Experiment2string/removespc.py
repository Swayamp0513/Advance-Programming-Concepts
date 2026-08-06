string = input("Enter a string: ")
nospace = ""
for char in string:
    if char != " ":
        nospace += char
print(f"String without spaces: {nospace}")
