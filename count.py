str = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
vowel  = "aeiouAEIOU"
for char in str :
    if char.isalpha():
        if char in vowel:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special += 1
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special Characters: {special}")
