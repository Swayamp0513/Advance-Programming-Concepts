import re

text = "Delivery locations: Mumbai 400001, Pune 411007, and Kolhapur 416004. Ignore 12345 or 9999999."
pincodes = re.findall(r'\b[1-9][0-9]{5}\b', text)

print("Extracted 6-digit PIN codes:", pincodes)
