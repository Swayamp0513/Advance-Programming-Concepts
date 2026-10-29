import re

text = input("Enter text with irregular spacing: ")
cleaned = re.sub(r'[ \t]+', ' ', text).strip()

print("Cleaned text:", cleaned)
