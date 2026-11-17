

name = input("Enter Employee Name: ")
print("Data type:", type(name))

emp_id = int(input("Enter Employee ID: "))
print("Data type:", type(emp_id))

salary = float(input("Enter Salary: "))
print("Data type:", type(salary))

department = input("Enter Department: ")
print("Data type:", type(department))

active = input("Is the employee active? (yes/no): ")
active = active.lower() == "yes"
print("Data type:", type(active))

print("\n--- Employee Details ---")
print("Name       :", name)
print("ID         :", emp_id)
print("Salary     :", salary)
print("Department :", department)
print("Active     :", active)

#Enter Employee Name: Priya Singh
#Enter Employee ID: 1002
#Enter Salary: 52000.75
#Enter Department: IT
#Is the employee active? (yes/no): yes