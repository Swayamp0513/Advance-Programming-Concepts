filename = input("Enter file name: ")
try:
    with open(filename, "r") as f:
        data = f.read()
        print("Total characters (including spaces):", len(data))
except FileNotFoundError:
    print("Error: File not found")
