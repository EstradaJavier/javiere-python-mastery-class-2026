# lessons/04_control_flow.py
# Python Mastery 2026 - Lesson 4: Control Flow
# Author: Javier P. Estrada
# Date: January 1, 2026
# Goal: Make decisions and repeat actions intelligently

"""
OBJECTIVES:
- if/elif/else
- for and while loops
- break, continue, else clauses
- Practice with real scenarios
"""

# -------------------------------------------------------
# Conditionals
# -------------------------------------------------------
rating = 100

if rating == 100:
    print("P&T - full benefits!")
elif rating >= 70:
    print("High rating - strong case")
else:
    print("Keep fighting")

# Ternary
status = "P&T" if rating == 100 else "In progress"
print(status)

# -------------------------------------------------------
# Loops
# -------------------------------------------------------
goals = ["Lesson complete", "Daily commit", "Family time"]

print("\nFor loop:")
for i, goal in enumerate(goals, 1):
    print(f"{i}. {goal}")

print("\nWhile loop:")
count = 0
while count < 3:
    print(f"Day {count + 1} of streak")
    count += 1

# Loop control
for skill in ["Python", "SQL", "Git", "Pandas"]:
    if skill == "SQL":
        continue  # Skip
    if skill == "Pandas":
        break     # Stop
    print(skill)

# -------------------------------------------------------
# Motivation
# -------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "="*60)
    print("NEW YEAR - LESSON 4 COMPLETE")
    print("="*60)
    print("Control flow = control of your future.")
    print("2026 starts with action. Keep the streak alive! 🚀")

# SELF-TEST QUIZ
"""
1. What prints if rating = 80?
2. Write ternary for "Adult" if age >= 18
3. What does continue do?
4. Loop else clause runs when?
5. Fix infinite while
6. Range(5) gives what?
7. Enumerate use case
8. Nested if example
9. Truthy/falsy values
10. while True pattern

# Answers in comments next lesson
"""