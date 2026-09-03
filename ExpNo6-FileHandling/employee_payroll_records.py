def load_employees(file_path):
    employees = []
    with open(file_path, "r") as f:
        for line in f:
            eid, name, dept, sal = line.strip().split(",")
            employees.append({'id': eid, 'name': name, 'dept': dept, 'salary': float(sal)})
    return employees

def display_all(employees):
    print("\nEmployee List:")
    for e in employees:
        print(f"{e['id']} | {e['name']} | {e['dept']} | Rs. {e['salary']}")

def highest_paid(employees):
    top = max(employees, key=lambda x: x['salary'])
    print(f"\nHighest Paid: {top['name']} ({top['salary']})")

def average_salary(employees):
    avg = sum(e['salary'] for e in employees) / len(employees)
    print(f"Average Salary: Rs. {avg:.2f}")

def earners_above(employees, threshold):
    print(f"\nEmployees earning above {threshold}:")
    for e in employees:
        if e['salary'] > threshold:
            print(f"{e['name']} : Rs. {e['salary']}")

with open("employees.txt", "w") as f:
    f.write("1,Karan,IT,65000\n2,Sneha,HR,48000\n3,Vikas,Finance,82000\n4,Pooja,IT,71000\n")

emp_list = load_employees("employees.txt")
display_all(emp_list)
highest_paid(emp_list)
average_salary(emp_list)
earners_above(emp_list, 60000)
