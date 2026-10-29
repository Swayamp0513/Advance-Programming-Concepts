import re

text = input("Enter a string with special characters: ")
cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)

print("Sanitized text:", cleaned)
