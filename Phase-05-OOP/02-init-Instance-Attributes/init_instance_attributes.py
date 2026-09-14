

class Employee:

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


# Creating objects
employee1 = Employee("Rahul", "Data Engineer", 60000)
employee2 = Employee("Aman", "Data Analyst", 50000)


# Accessing instance attributes
print(employee1.name)
print(employee1.role)
print(employee1.salary)

print()

print(employee2.name)
print(employee2.role)
print(employee2.salary)