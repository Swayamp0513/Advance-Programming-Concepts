import re

text = input("Enter a string: ")
uppercase_letters = re.findall(r'[A-Z]', text)

print("Uppercase letters:", uppercase_letters)
