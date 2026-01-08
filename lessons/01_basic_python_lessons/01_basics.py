# ===================================
# 01_basics.py
# Python Mastery 2026 - Lesson 1: Python Basics and Foundations
# ===================================

# Lesson Objectives (Based on Bloom's Taxonomy)
# - Knowledge: Understand Python's history, uses, and career potential.
# - Comprehension: Explain basic syntax, variables, and data types through comments.
# - Application: Apply concepts in code examples and exercises.
# - Analysis: Self-assess learning with automated tests (Codeup-style asserts for immediate feedback).
# - Best Practices: Follow PEP 8 (Python Enhancement Proposal 8) for code style – e.g., 4-space indentation, max 79 chars per line.

# Introduction to Python
# Python is a high-level, interpreted programming language known for its readability and versatility.
# It was created by Guido van Rossum in 1991 as a successor to ABC language, emphasizing code readability with significant whitespace.
# Guido van Rossum (Dutch programmer) started it at Centrum Wiskunde & Informatica in the Netherlands.
# Who uses Python? Major companies like Google (search engine), Netflix (recommendation systems), NASA (scientific computing), Instagram (backend), and Spotify (data analysis).
# Applications: Web development (Django/Flask), data science (Pandas/NumPy), AI/ML (TensorFlow/PyTorch), automation (scripts for tasks like file management), and more.
# In AI and LLM: Python is the de facto language for training models (e.g., OpenAI's GPT uses Python libraries). We'll explore this in later lessons, including how Python interfaces with APIs like OpenAI's for LLM integration.

# Career Potential (2025 US Averages from Glassdoor, Built In, and Indeed)
# - Beginner/Junior Developer (0-2 years): $80,000 - $100,000/year (start with bootcamps or self-study; focus on building a portfolio on GitHub).
# - Senior Developer (5+ years): $130,000 - $170,000/year (specialize in AI/data; high demand in tech hubs like San Francisco).
# - Development Manager (10+ years, leading teams): $160,000 - $220,000/year (combine technical skills with leadership; roles at FAANG companies can exceed $250,000 with bonuses).
# Tips: Get certified (Python Institute PCAP), contribute to open-source, network on LinkedIn. From here: Master basics, then data structures (Lesson 2), functions (Lesson 4), and AI applications (Lesson 10+).

print("Welcome to Python Mastery 2026 - Lesson 1: Basics")
print("Let's explore variables, data types, and operations.\n")

# Basic Variables (Comprehension and Application)
# Variables store data. No need to declare type – Python is dynamically typed.
name = "Javier"  # str (string): Text data, enclosed in quotes.
age = 35  # int (integer): Whole numbers for calculations like age.
height = 1.75  # float (floating-point): Decimal numbers for precision, e.g., height in meters.
is_veteran = True  # bool (boolean): True/False values for conditions.

# Print with f-strings (Python 3.6+): Easy formatting for readability.
print(f"Name: {name} (type: {type(name)})")  # type() shows data type.

print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} m (type: {type(height)})")
print(f"Is veteran: {is_veteran} (type: {type(is_veteran)})\n")

# Basic Operations (Application: Math and String Manipulation)
# Operators: + (add), - (subtract), * (multiply), / (divide), // (floor divide), % (modulo).
years_to_retirement = 65 - age  # int subtraction.
height_feet = height * 3.28084  # float multiplication for conversion.
print(f"Years to retirement (65 - age): {years_to_retirement}")
print(f"Height in feet: {round(height_feet, 2)}")  # round() for clean output.
print(f"Concatenated string: {name + ' is ' + str(age) + ' years old.'}")  # Type conversion with str().

# f-strings for modern, readable concatenation (best practice over + for strings).
print(f"f-string example: {name} is {age} years old and {height}m tall.\n")

# Input for Interactivity (Active Learning: User Engagement)
# Uncomment to test – input() pauses for user entry.
# favorite_lang = input("What's your favorite programming language? ")
# print(f"You said: {favorite_lang}")

# Self-Assessment Test (Codeup-Style: Automated Asserts for Active Recall)
# Run the file to see if tests pass – simulates unit testing (we'll use pytest in later lessons).
def self_test():
    # Test 1: Basic variable assignment and type.
    assert type(name) == str, "Name should be a string."
    assert age == 35, "Age should be 35."

    # Test 2: Operation result.
    assert years_to_retirement == 30, "Years to retirement calculation failed."

    # Test 3: Type conversion.
    age_str = str(age)
    assert type(age_str) == str, "Age not converted to string."

    print("All self-tests passed – you've grasped the basics!")

if __name__ == "__main__":  # Runs only when file is executed directly (best practice for tests).
    self_test()

# Where to Go From Here
# Next: Lesson 2 - Strings and Lists (data manipulation, common in AI for text processing).
# Then: Functions, OOP, then AI/LLM (e.g., Python in machine learning libraries like scikit-learn).
# Practice: Write a script to calculate your salary growth (beginner to senior) using variables.
# Resource: Python.org docs, "Python for Beginners" on Coursera, or freeCodeCamp YouTube series.

print("\nLesson 1 complete. Review comments, run tests, and experiment!")

