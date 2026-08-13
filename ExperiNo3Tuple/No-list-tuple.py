numberslist = []
for i in range(5):
    num = int(input("Enter a number: "))
    numberslist.append(num)
numberstuple = tuple(numberslist)
print("Final tuple:", numberstuple)