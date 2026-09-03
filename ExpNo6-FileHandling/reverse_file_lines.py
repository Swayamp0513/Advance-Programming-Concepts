filename = input("Enter file name: ")
try:
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in reversed(lines):
        print(line.rstrip())
except FileNotFoundError:
    print("Error: File not found")
