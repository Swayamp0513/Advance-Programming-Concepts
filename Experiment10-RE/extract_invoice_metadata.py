import re

invoice_text = """Invoice INV-9821 issued on 12-04-2026. Total Amount: $450.00.
Earlier Invoice INV-1044 dated 01-03-2026 had due amount Rs. 12500.50."""

invoice_numbers = re.findall(r'\bINV-\d+\b', invoice_text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', invoice_text)
amounts = re.findall(r'(?:\$|Rs\.\s*)(\d+(?:\.\d{2})?)', invoice_text)

print("Invoice Numbers:", invoice_numbers)
print("Dates:", dates)
print("Monetary Amounts:", amounts)
