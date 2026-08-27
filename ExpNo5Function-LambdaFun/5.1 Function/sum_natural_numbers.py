def sum_n_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter n: "))
print("Sum of natural numbers:", sum_n_natural(n))
