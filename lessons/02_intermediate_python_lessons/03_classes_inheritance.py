# 03_classes_inheritance.py
# Inheritance allows a child class to inherit attributes/methods from a parent class.
# This promotes code reuse. Polymorphism lets child classes override parent methods for custom behavior.
# We'll create a 'Employee' class inheriting from 'Person', adding salary and overrides.

class Person:  # Parent (base) class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}, {self.age} years old."

class Employee(Person):  # Child class inherits from Person (put parent in parentheses).
    def __init__(self, name, age, salary):  # Extend __init__.
        super().__init__(name, age)  # Call parent's __init__ using super() — inherits name/age.
        self.salary = salary         # Add new attribute.

    def greet(self):  # Override parent's greet method (polymorphism).
        # Call parent's greet with super() and add more.
        return super().greet() + f" I earn ${self.salary} annually."

    def give_raise(self, percentage):  # New method unique to Employee.
        increase = self.salary * (percentage / 100)
        self.salary += increase
        return f"New salary: ${self.salary}"

# Create objects.
person = Person("Eve", 40)
employee = Employee("Frank", 32, 60000)

# Use inherited and overridden methods.
print(person.greet())    # Expected: "Hello, I'm Eve, 40 years old."
print(employee.greet())  # Expected: "Hello, I'm Frank, 32 years old. I earn $60000 annually."

# Use child-specific method.
print(employee.give_raise(10))  # Expected: "New salary: $66000.0"

# Inheritance note: Employee has access to Person's attributes/methods, but not vice versa.
# Common pitfall: Forgetting super() can lead to uninitialized parent attributes.
# Exercise: Create a 'Manager' class inheriting from Employee, with a 'team_size' attribute and override give_raise to include bonuses.

# Expected overall output:
# Hello, I'm Eve, 40 years old.
# Hello, I'm Frank, 32 years old. I earn $60000 annually.
# New salary: $66000.0