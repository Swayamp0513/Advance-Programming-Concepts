import re

code = input("Enter product code (format: ABC-1234-XY): ").strip()
pattern = r'^[A-Z]{3}-\d{4}-[A-Z]{2}$'

if re.match(pattern, code):
    print("Valid product code format.")
else:
    print("Invalid product code format.")
