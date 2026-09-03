filename = input("Enter filename to open: ")
try:
    with open(filename, "r") as f:
        print("\nFile Contents:")
        print(f.read())
except FileNotFoundError:
    print("Error: File not found")
