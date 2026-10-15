import re

sentence = input("Enter a sentence: ")
words_five = re.findall(r'\b[a-zA-Z]{5}\b', sentence)

print("Words containing exactly 5 characters:", words_five)
