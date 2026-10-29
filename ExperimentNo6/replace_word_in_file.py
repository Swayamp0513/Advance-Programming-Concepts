filename = input("Enter file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")

try:
    with open(filename, "r") as f:
        data = f.read()
    updated_data = data.replace(old_word, new_word)
    with open(filename, "w") as f:
        f.write(updated_data)
    print(f"Replaced all occurrences of '{old_word}' with '{new_word}'.")
except FileNotFoundError:
    print("Error: File not found")
