import re

text = "Files saved: report.pdf, archive.tar.gz, script.py, picture.jpeg, notes.txt"
extensions = re.findall(r'\b\w+\.([a-zA-Z0-9]+)\b', text)

print("Extracted extensions:", extensions)
