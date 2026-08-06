str  = input("Enter a string: ")
reversed = ""
for char in str:
    reversed = char + reversed
if str.lower() == reversed.lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
