def calculate_gross_salary(basic):
    hra = 0.20 * basic
    da = 0.50 * basic
    return basic + hra + da



b_salary = float(input("Enter basic salary: "))
print("Gross Salary:", calculate_gross_salary(b_salary))
