with open("attendance.txt", "w") as f:
    f.write("Rohan,40,48\nSimran,32,48\nAditya,45,48\nNeha,28,48\n")

print("Students with attendance below 75%:")
with open("attendance.txt", "r") as f:
    for line in f:
        name, attended, total = line.strip().split(",")
        percentage = (int(attended) / int(total)) * 100
        if percentage < 75:
            print(f"{name}: {percentage:.2f}%")
