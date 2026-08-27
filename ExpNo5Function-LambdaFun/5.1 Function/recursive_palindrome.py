def is_palindrome_recursive(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])




text = input("Enter string: ")
print("Is Palindrome:", is_palindrome_recursive(text))
