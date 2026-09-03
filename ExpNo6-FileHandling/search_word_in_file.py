filename = input("Enter file name: ")
target = input("Enter word to search: ").lower()

occurrences = 0
line_numbers = []

try:
    with open(filename, "r") as f:
        for line_no, line in enumerate(f, start=1):
            words = [w.strip(".,!?;:").lower() for w in line.split()]
            count = words.count(target)
            if count > 0:
                occurrences += count
                line_numbers.append(line_no)
    print("Total occurrences:", occurrences)
    print("Found on line(s):", line_numbers)
except FileNotFoundError:
    print("Error: File not found")
