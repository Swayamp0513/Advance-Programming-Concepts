import re

sentence = input("Enter a sentence: ")
words_s = re.findall(r'\b\w+[sS]\b', sentence)

print("Words ending with 's':", words_s)
