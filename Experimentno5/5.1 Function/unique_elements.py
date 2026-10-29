def get_unique(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

items = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", items)
print("Unique List:", get_unique(items))
