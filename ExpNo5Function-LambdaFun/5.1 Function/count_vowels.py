def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count




text = input("Enter a string: ")
print("Vowel count:", count_vowels(text))
