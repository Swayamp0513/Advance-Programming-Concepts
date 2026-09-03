src = input("Enter python file to read: ")
dest = input("Enter output file name: ")

try:
    with open(src, "r") as infile, open(dest, "w") as outfile:
        for line in infile:
            stripped = line.lstrip()
            if not stripped.startswith("#"):
                outfile.write(line)
    print("Comments removed successfully.")
except FileNotFoundError:
    print("Error: Input file does not exist.")
