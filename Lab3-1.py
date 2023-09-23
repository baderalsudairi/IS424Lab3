
employee_salaries = {}


while True:
    name = input("Enter the employee's name (or 'no' to quit): ")

 
    if name.lower() == 'no':
        break

    salary = float(input("Enter the employee's salary: "))

 
    employee_salaries[name] = salary


print("Employee salaries:")
for name, salary in employee_salaries.items():
    print(f"{name}: ${salary:.2f}")
