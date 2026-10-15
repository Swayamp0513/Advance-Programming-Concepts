import re

vehicle_no = input("Enter vehicle number (e.g., MH12AB1234): ").strip().upper()
pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$'

if re.match(pattern, vehicle_no):
    print("Valid Indian vehicle registration number.")
else:
    print("Invalid vehicle registration format.")
