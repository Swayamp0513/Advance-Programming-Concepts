def analyze_list(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num
    avg = total / len(numbers)
    return minimum, maximum, total, avg
nums = [15, 3, 9, 22, 11]
mn, mx, sm, av = analyze_list(nums)
print(f"Min: {mn}, Max: {mx}, Sum: {sm}, Avg: {av}")
