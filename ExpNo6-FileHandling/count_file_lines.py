filename = input("Enter file name: ")
try:
    with open(filename, "r") as f:
        lines = f.readlines()
        print("Total number of lines:", len(lines))
except FileNotFoundError:
    print("Error: File not found")
