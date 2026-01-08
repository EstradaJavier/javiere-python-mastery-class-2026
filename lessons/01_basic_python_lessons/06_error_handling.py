# lessons/06_error_handling.py
# Python Mastery 2026 - Lesson 6: Error Handling
# Author: Javier P. Estrada
# Date: January 3, 2026

try:
    salary = int(input("Enter salary: "))
except ValueError:
    print("Invalid number - using 0")
    salary = 0
finally:
    print("Processing complete")

# Custom exception
class GoalNotReached(Exception):
    pass

# Raise
if salary < 150000:
    raise GoalNotReached("Keep pushing!")

if __name__ == "__main__":
    print("Lesson 6 complete - resilient code = resilient life 🚀")