import re

text = """Check the docs at https://docs.python.org/3/ or browse http://example.com/index.html
and secure portal https://portal.college.edu."""

urls = re.findall(r'https?://[^\s]+', text)
print("Web addresses found:", urls)
