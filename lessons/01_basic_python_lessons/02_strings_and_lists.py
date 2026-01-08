# ===================================
# 02_strings_and_lists.py
# Python Mastery 2026 - Lesson 2: Strings and Lists
# ===================================

# Lesson Objectives (Bloom's Taxonomy)
# - Knowledge: Understand strings and lists, their methods, and Python's role in data manipulation.
# - Comprehension: Explain operations through comments.
# - Application: Use methods in examples and exercises.
# - Analysis: Self-assess with automated tests (asserts for immediate feedback, Codeup-style).
# - Best Practices: Use list comprehensions for efficiency, str methods for readability (PEP 8).
# - Learning Methods: Active recall via tests, spaced repetition by reviewing Lesson 1 concepts in context.

# Introduction to Strings and Lists
# Strings are immutable sequences of characters, ideal for text (e.g., NLP in AI/LLM – Python's str is used in Hugging Face libraries for tokenization).
# Lists are mutable sequences of items, great for dynamic data (e.g., storing LLM output tokens or datasets in pandas).
# Who started Python? Guido van Rossum (1991) – strings/lists are core, inspired by ABC language.
# Who uses them? FAANG companies (Google's search uses string matching; Amazon's recommendations use lists for data).
# Potential Wages (2025 US averages from Glassdoor/BLS): Beginner Python dev: $80k-$100k (string/list skills in entry scripts). Senior: $130k-$170k (AI data processing). Manager: $160k-$220k (overseeing ML teams).
# In AI/LLM: Strings for text preprocessing (e.g., cleaning prompts for GPT). Lists for batching data in PyTorch. From here: Next lessons build to AI (Lesson 10: Python in LLM APIs like OpenAI).
# Resource: "Python Crash Course" book or fast.ai for AI applications.

print("Welcome to Lesson 2: Strings and Lists")
print("Let's explore operations, methods, and AI ties.\n")

# Strings (Comprehension and Application)
# Strings are immutable – can't change in place, but can create new ones.
greeting = "Hello, Python Mastery!"
print(f"Original string: {greeting}")

# Methods: upper/lower (case change), strip (remove whitespace), replace (swap text).
upper_greeting = greeting.upper()
stripped = greeting.strip("!")  # Removes '!' from ends.
replaced = greeting.replace("Hello", "Hi")
print(f"Upper: {upper_greeting}")
print(f"Stripped '!': {stripped}")
print(f"Replaced 'Hello' with 'Hi': {replaced}")

# Slicing: [start:end:step] – useful in AI for token slicing.
slice1 = greeting[0:5]  # "Hello"
slice2 = greeting[::-1]  # Reversed: "!yretsaM nohtyP ,olleH"
print(f"Slice [0:5]: {slice1}")
print(f"Reversed: {slice2}\n")

# Lists (Comprehension and Application)
# Lists are mutable – can add/remove items (e.g., dynamic data in LLM training loops).
skills = ["Python", "AI", "Data Science", "LLM"]
print(f"Original list: {skills}")

# Methods: append (add end), insert (add at index), pop (remove end), sort (alphabetical).
skills.append("Git")
skills.insert(1, "Strings")
skills.pop()  # Removes last ("Git").
skills.sort()  # Sorts in place.
print(f"After append/insert/pop/sort: {skills}")

# List Comprehension: Efficient way to create lists (spaced repetition: like loops from Lesson 1).
lengths = [len(skill) for skill in skills]  # [len of each string].
print(f"Lengths via comprehension: {lengths}\n")

# Self-Assessment Test (Codeup-Style: Asserts for Immediate Feedback)
# Run to check learning – if all pass, you've mastered the concepts.
def self_test():
    # Test 1: String methods.
    assert upper_greeting == "HELLO, PYTHON MASTERY!", "upper() failed."
    assert slice2 == "!yretsaM nohtyP ,olleH", "Slicing reversed failed."

    # Test 2: List operations.
    assert "Strings" in skills, "insert() failed."
    assert len(skills) == 5, "pop() failed to remove last item."
    assert lengths == [2, 6, 8, 3, 6], "List comprehension failed."  # Adjust if skills change.

    print("All self-tests passed – excellent retention!")

if __name__ == "__main__":
    self_test()

# Where to Go From Here
# Next: Lesson 3 – Dictionaries and Sets (key for AI data storage, e.g., JSON in LLM APIs).
# Practice: Write a list of AI skills, sort it, and use string methods to format.
# Career Tip: Master lists/strings for data roles – entry jobs often involve text processing in Python for $80k+.

print("\nLesson 2 complete. Run tests, experiment, and push to Git! Questions? Ask Grok.")