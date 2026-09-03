def count_vowels(s):
    return sum(1 for ch in s if ch in "aeiouAEIOU")

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_words(s):
    return len(s.split())

def remove_spaces(s):
    return s.replace(" ", "")
