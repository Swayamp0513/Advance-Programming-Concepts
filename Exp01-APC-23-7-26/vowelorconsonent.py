char = input("Enter a single character: ")
if char in 'aeiou':
    print(f"{char} is a Vowel")
elif char in 'AEIOU':
    print(f"{char} is a Vowel")
else:
    print(f"{char} is a Consonant")
