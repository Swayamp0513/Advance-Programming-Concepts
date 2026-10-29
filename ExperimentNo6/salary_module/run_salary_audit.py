import salary_calculator

basic = float(input("Enter basic salary: "))
gross = salary_calculator.calculate_gross(basic)
deductions = salary_calculator.calculate_deductions(gross)
net = salary_calculator.calculate_net(basic)

print(f"Gross Salary: Rs. {gross:.2f}")
print(f"Total Deductions: Rs. {deductions:.2f}")
print(f"Net Salary: Rs. {net:.2f}")
