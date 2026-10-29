def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_digits(n):
    return n if n < 10 else (n % 10) + sum_of_digits(n // 10)

def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)
