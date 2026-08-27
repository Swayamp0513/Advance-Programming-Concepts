def list_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

nums = [10, 20, 30, 40, 50]
print("List:", nums)
print("Average:", list_average(nums))
