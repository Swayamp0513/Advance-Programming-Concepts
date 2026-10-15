import re

text = input("Enter a string: ")
digits = re.findall(r'\d', text)

print("Extracted digits:", digits)
print("Joined digits:", "".join(digits))
