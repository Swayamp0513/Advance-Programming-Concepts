def reverse_string(text):
    rev = ""
    for char in text:
        rev = char + rev
    return rev





text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
