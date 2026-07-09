# 02_classes_methods_attributes.py
# This script explores more on classes: instance attributes (unique per object), class attributes (shared),
# instance methods (operate on self), class methods (operate on the class), and static methods (utility functions).
# We'll extend the 'Person' class with job tracking and a shared company name.

class Person:
    # Class attribute: Shared by all instances. Defined outside methods.
    company = "TechCorp"  # All persons work at the same fictional company.

    def __init__(self, name, age, job="Developer"):
        self.name = name      # Instance attribute: Unique to each object.
        self.age = age
        self.job = job        # Default value if not provided.

    # Instance method: Accesses instance attributes via self.
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, working as {self.job} at {self.company}."

    # Class method: Operates on the class, not instance. Uses @classmethod decorator and 'cls' parameter.
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company  # Changes the shared class attribute.
        return f"Company changed to {new_company} for all employees."

    # Static method: Utility function, no self/cls. Uses @staticmethod decorator.
    @staticmethod
    def calculate_bonus(salary, percentage):
        return salary * (percentage / 100)  # Simple calc, no access to class/instance data.

# Create instances.
emp1 = Person("Charlie", 35, "Engineer")
emp2 = Person("Dana", 28)

# Print introductions.
print(emp1.introduce())  # Expected: "Hi, I'm Charlie, 35 years old, working as Engineer at TechCorp."
print(emp2.introduce())  # Expected: "Hi, I'm Dana, 28 years old, working as Developer at TechCorp."

# Access class attribute (same for both).
print(f"emp1 company: {emp1.company}")  # Expected: "emp1 company: TechCorp"

# Use class method to change shared attribute (universal change).
print(Person.change_company("InnoTech"))  # Expected: "Company changed to InnoTech for all employees."
print(emp1.introduce())  # Now: "... at InnoTech."
print(emp2.introduce())  # Same for emp2.

# Use static method (no object needed).
bonus = Person.calculate_bonus(50000, 10)
print(f"Bonus: {bonus}")  # Expected: "Bonus: 5000.0"

# Common pitfall: Class attributes can be overridden per instance (e.g., emp1.company = "Other"), but changes won't affect others.
# Exercise: Add a @staticmethod to convert age to dog years (age * 7).

# Expected overall output:
# Hi, I'm Charlie, 35 years old, working as Engineer at TechCorp.
# Hi, I'm Dana, 28 years old, working as Developer at TechCorp.
# emp1 company: TechCorp
# Company changed to InnoTech for all employees.
# Hi, I'm Charlie, 35 years old, working as Engineer at InnoTech.
# Hi, I'm Dana, 28 years old, working as Developer at InnoTech.
# Bonus: 5000.0