import re

sentence = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', sentence)

print("Identified words:", words)
print("Total word count:", len(words))
