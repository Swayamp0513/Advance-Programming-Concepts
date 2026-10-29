with open("file_one.txt", "w") as f:
    f.write("Line from first file.\nAnother line from first file.\n")

with open("file_two.txt", "w") as f:
    f.write("Line from second file.\nAnother line from second file.\n")

with open("file_one.txt", "r") as f1, open("file_two.txt", "r") as f2, open("merged_output.txt", "w") as out:
    out.write(f1.read())
    out.write(f2.read())

print("Files merged successfully into merged_output.txt")
