filename = input("Enter file name: ")
try:
    with open(filename, "r") as f:
        for index, line in enumerate(f, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print("Error: File not found")
