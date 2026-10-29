import re

sentence = input("Enter a sentence: ")
matches = re.findall(r'\b[aA]\w*', sentence)

print("Words beginning with 'A' or 'a':", matches)
