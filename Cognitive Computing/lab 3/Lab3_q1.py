
class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, emp_id, department, salary, team_size):
        super().__init__(name, emp_id, department, salary)
        self.team_size = team_size

    def display(self):
        print("Frame: Manager")
        super().display()
        print(f"Team Size: {self.team_size}")
        print("(Inherited from Employee frame)")

role = input("Enter role: ")

if role.lower() == "manager":
    name = input("Enter Name: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))
    team_size = int(input("Enter Team Size: "))

    manager = Manager(name, emp_id, department, salary, team_size)
    print()
    manager.display()
else:
    print("Invalid role")
