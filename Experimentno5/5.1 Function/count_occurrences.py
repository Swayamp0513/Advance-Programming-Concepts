def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
items = [1, 2, 3, 2, 4, 2, 5, 5]
target = int(input("Enter number: "))
print("List:", items)
print(f"Occurrences of {target}:", count_occurrences(items, target))
