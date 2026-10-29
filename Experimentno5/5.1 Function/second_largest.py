def second_largest(numbers):
    unique_nums = list(set(numbers))
    unique_nums.sort()
    return unique_nums[-2]





nums = [12, 45, 2, 45, 34, 10]
print("List:", nums)
print("Second largest:", second_largest(nums))
