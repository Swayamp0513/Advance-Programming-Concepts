def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    return result




b = float(input("Enter base: "))
e = int(input("Enter exponent: "))
print("Power:", power(b, e))
