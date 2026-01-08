# lessons/08_oop_basics.py
# Python Mastery 2026 - Lesson 8: Object-Oriented Programming
# Author: Javier P. Estrada
# Date: January 5, 2026

class Veteran:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def status(self):
        return f"{self.name}: {self.rating}% P&T"

    def motivate(self):
        return "One lesson at a time!"

javier = Veteran("Javier P. Estrada", 100)
print(javier.status())
print(javier.motivate())

if __name__ == "__main__":
    print("Lesson 8 complete - OOP powers real applications 🚀")