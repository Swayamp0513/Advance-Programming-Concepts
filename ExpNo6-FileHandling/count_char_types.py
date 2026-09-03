filename = input("Enter file name: ")
alphabets = 0
digits = 0
spaces = 0
specials = 0

try:
    with open(filename, "r") as f:
        text = f.read()
        for ch in text:
            if ch.isalpha():
                alphabets += 1
            elif ch.isdigit():
                digits += 1
            elif ch.isspace():
                spaces += 1
            else:
                specials += 1
    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Special Characters:", specials)
except FileNotFoundError:
    print("Error: File not found")
