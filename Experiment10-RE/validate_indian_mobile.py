import re

phone = input("Enter 10-digit Indian mobile number: ").strip()
pattern = r'^[6-9]\d{9}$'

if re.match(pattern, phone):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")
