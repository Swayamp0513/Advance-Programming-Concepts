import re

paragraph = """Important dates: Submission on 15-08-2026, verification on 02-09-2026,
and final presentation scheduled on 31-12-2026."""

dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', paragraph)
print("Extracted Dates (DD-MM-YYYY):", dates)
