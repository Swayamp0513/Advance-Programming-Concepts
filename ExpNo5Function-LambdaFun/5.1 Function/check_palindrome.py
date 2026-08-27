def is_palindrome(value):
    s = str(value)
    return s == s[::-1]
val = input("Enter string or number: ")
print("Is Palindrome:", is_palindrome(val))
