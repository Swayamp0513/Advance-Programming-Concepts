def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"



num = int(input("Enter number: "))
print("Result:", even_odd(num))
