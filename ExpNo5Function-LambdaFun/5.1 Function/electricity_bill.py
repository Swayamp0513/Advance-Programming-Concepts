def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + (units - 100) * 7
    else:
        return (100 * 5) + (100 * 7) + (units - 200) * 10



u = float(input("Enter electricity units: "))
print("Electricity Bill Amount:", calculate_bill(u))
