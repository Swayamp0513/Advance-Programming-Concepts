import re

text = "Sample line with spaces.\tAlso a tab here.\nAnd a newline character."

spaces = re.findall(r' ', text)
tabs = re.findall(r'\t', text)
newlines = re.findall(r'\n', text)

print("Original text representation:")
print(repr(text))
print("Space count:", len(spaces))
print("Tab count:", len(tabs))
print("Newline count:", len(newlines))
