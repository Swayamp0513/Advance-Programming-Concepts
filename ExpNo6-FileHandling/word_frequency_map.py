filename = input("Enter file name: ")
freq = {}
try:
    with open(filename, "r") as f:
        for word in f.read().split():
            w = word.strip(".,!?;:\"\'").lower()
            if w:
                freq[w] = freq.get(w, 0) + 1
    print("Word occurrences:")
    for word, count in freq.items():
        print(f"{word}: {count}")
except FileNotFoundError:
    print("Error: File not found")
