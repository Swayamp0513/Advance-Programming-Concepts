def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest




nums = [10, 45, 2, 99, 34]
print("Numbers:", nums)
print("Largest element:", find_largest(nums))
