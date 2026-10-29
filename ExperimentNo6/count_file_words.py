filename = input("Enter file name: ")
try:
    with open(filename, "r") as f:
        content = f.read()
        words = content.split()
        print("Total words:", len(words))
except FileNotFoundError:
    print("Error: File not found")
