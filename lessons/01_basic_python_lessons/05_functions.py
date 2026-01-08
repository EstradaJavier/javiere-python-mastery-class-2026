# lessons/05_functions.py
# Python Mastery 2026 - Lesson 5: Functions
# Author: Javier P. Estrada
# Date: January 2, 2026
# Goal: Write reusable, clean code

def calculate_needed(current: int, goal: int = 150000) -> int:
    """Return how much salary increase needed"""
    return max(goal - current, 0)

def greet(name: str = "Javier") -> str:
    return f"Hello {name}! Keep learning."

# Default, positional, keyword args
print(calculate_needed(80000))
print(calculate_needed(current=100000, goal=200000))

# Variable args
def log_goals(*goals: str) -> None:
    for g in goals:
        print(f"Goal: {g}")

log_goals("MSAI", "High salary", "Family security")

# Lambda
double = lambda x: x * 2
print(double(5))

if __name__ == "__main__":
    print("\n" + "="*60)
    print("LESSON 5 COMPLETE")
    print("="*60)
    print("Functions = building blocks of your future code.")
    print("You're unstoppable! 🚀")

# QUIZ (answers next time)