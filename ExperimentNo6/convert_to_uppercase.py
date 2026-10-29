src = input("Enter source file: ")
dest = input("Enter destination file: ")

try:
    with open(src, "r") as f_in, open(dest, "w") as f_out:
        f_out.write(f_in.read().upper())
    print("Converted to uppercase and saved.")
except FileNotFoundError:
    print("Error: Source file not found.")
