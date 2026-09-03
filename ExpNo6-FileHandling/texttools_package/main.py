from texttools.cleaning import clean_text
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

raw = "Hello, world!  This is a clean, simple world."
cleaned = clean_text(raw)
tokens = tokenize(cleaned)
freq = word_frequency(tokens)

print("Cleaned:", cleaned)
print("Tokens:", tokens)
print("Frequencies:", freq)
