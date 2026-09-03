filename = input("Enter file name: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

try:
    with open(filename, "r") as f:
        text = f.read()
        for ch in text:
            if ch.isalpha():
                if ch in vowels:
                    v_count += 1
                else:
                    c_count += 1
    print("Vowels:", v_count)
    print("Consonants:", c_count)
except FileNotFoundError:
    print("Error: File not found")
