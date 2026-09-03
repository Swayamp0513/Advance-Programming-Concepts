import calculator

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print("Result:", calculator.add(x, y))
elif op == '-':
    print("Result:", calculator.subtract(x, y))
elif op == '*':
    print("Result:", calculator.multiply(x, y))
elif op == '/':
    print("Result:", calculator.divide(x, y))
else:
    print("Invalid Opoerator")
