with open("doc_a.txt", "w") as f:
    f.write("Alpha\nBeta\nGamma\nDelta\n")

with open("doc_b.txt", "w") as f:
    f.write("Alpha\nBeta\nTheta\nDelta\n")

with open("doc_a.txt", "r") as f1, open("doc_b.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

identical = True
limit = min(len(lines1), len(lines2))

for i in range(limit):
    if lines1[i] != lines2[i]:
        print(f"Files differ at line {i + 1}:")
        print(f"File 1: {lines1[i].strip()}")
        print(f"File 2: {lines2[i].strip()}")
        identical = False
        break

if identical and len(lines1) != len(lines2):
    print(f"Files differ in length starting at line {limit + 1}")
elif identical:
    print("Both files are identical.")
