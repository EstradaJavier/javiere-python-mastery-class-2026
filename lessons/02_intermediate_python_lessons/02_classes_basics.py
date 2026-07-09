# 01_classes_basics.py
# This script demonstrates the basics of classes in Python.
# Classes are blueprints for creating objects. Objects are instances of classes.
# Think of a class as a template (e.g., a car design) and an object as a real thing made from it (e.g., a specific car).
# We'll create a simple 'Person' class to store name and age, and add a method to greet.

# Define the class using the 'class' keyword. Class names are usually Capitalized (CamelCase).
class Person:
    # The __init__ method is a special constructor method. It's called automatically when you create an object.
    # 'self' refers to the instance itself — it's like 'this' in other languages. Always include it as the first parameter.
    def __init__(self, name, age):  # Parameters: name and age are passed when creating the object.
        self.name = name  # Assign 'name' to the object's attribute (self.name). This stores data on the object.
        self.age = age    # Similarly for age. Attributes are like variables attached to the object.

    # A method is a function inside a class. It can access the object's attributes via 'self'.
    def greet(self):  # No extra parameters needed here, but 'self' is always required.
        # Use f-string for formatted output. Access self.name and self.age.
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create objects (instances) from the class.
# Syntax: object_name = ClassName(arguments for __init__)
person1 = Person("Alice", 30)  # Creates an object with name="Alice", age=30.
person2 = Person("Bob", 25)    # Another object, independent of person1.

# Access attributes using dot notation (object.attribute).
print(f"Person1 name: {person1.name}")  # Expected result: "Person1 name: Alice"
print(f"Person1 age: {person1.age}")    # Expected result: "Person1 age: 30"

# Call the method using dot notation (object.method()).
print(person1.greet())  # Expected result: "Hello, my name is Alice and I am 30 years old."
print(person2.greet())  # Expected result: "Hello, my name is Bob and I am 25 years old."

# You can add or modify attributes dynamically (but it's better to define them in __init__ for clarity).
person1.city = "New York"  # Adds a new attribute to person1 only.
print(f"Person1 city: {person1.city}")  # Expected result: "Person1 city: New York"

# Common pitfall: Forgetting 'self' in methods will cause errors.
# Exercise: Add a method 'birthday' that increases age by 1 and prints a message.

# Expected overall output when run:
# Person1 name: Alice
# Person1 age: 30
# Hello, my name is Alice and I am 30 years old.
# Hello, my name is Bob and I am 25 years old.
# Person1 city: New York