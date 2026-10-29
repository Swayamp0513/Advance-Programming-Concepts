import re

password = input("Enter password to evaluate: ")

length_check = len(password) >= 8
upper_check = bool(re.search(r'[A-Z]', password))
lower_check = bool(re.search(r'[a-z]', password))
digit_check = bool(re.search(r'\d', password))
special_check = bool(re.search(r'[^a-zA-Z0-9]', password))

if length_check and upper_check and lower_check and digit_check and special_check:
    print("Password is strong and meets all requirements.")
else:
    print("Weak password. Ensure 8+ chars, upper, lower, digit, and special char.")
