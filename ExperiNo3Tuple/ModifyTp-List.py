originaltuple = (10, 20, 30)
list = list(originaltuple)
list[1] = 99
modifiedtuple = tuple(list)
print(modifiedtuple)