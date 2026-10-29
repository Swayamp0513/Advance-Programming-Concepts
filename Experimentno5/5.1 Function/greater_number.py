def find_greater(a, b):
    if a > b:
        return a
    return b
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("Greater number:", find_greater(n1, n2))
