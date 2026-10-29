def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(operation, a, b):
    return operation(a, b)
print("Add:", calculate(add, 10, 5))
print("Multiply:", calculate(multiply, 10, 5))
