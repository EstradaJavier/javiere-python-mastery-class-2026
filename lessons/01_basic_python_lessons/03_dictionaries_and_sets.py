# lessons/03_dictionaries_and_sets.py
# Python Mastery 2026 - Lesson 3: Dictionaries & Sets
# Author: Javier P. Estrada
# Date: December 31, 2025
# Goal: Master key-value storage and unique collections – essential for real-world data

"""
OBJECTIVES:
- Use dicts for fast lookups (O(1))
- Understand sets for uniqueness and math operations
- Practice comprehensions
- Complete self-test
"""

# -------------------------------------------------------
# Dictionaries - Key-Value Pairs
# -------------------------------------------------------
profile = {
    "name": "Javier P. Estrada",
    "age": 35,
    "rating": 100,
    "goals": ["MSAI", "$150k+", "Wife's retirement"]
}

print("=== Dictionaries ===")
print(profile["name"])
print(profile.get("height", "Not found"))  # Safe access

# Add/update
profile["location"] = "Salado, TX"
profile["age"] = 36

# Methods
print(list(profile.keys()))
print(list(profile.values()))
print(list(profile.items()))

# Remove
del profile["location"]
popped = profile.pop("age")

# Update from another dict
updates = {"motivation": "Family", "daily_commit": True}
profile.update(updates)
print(profile)

# -------------------------------------------------------
# Sets - Unique Items
# -------------------------------------------------------
skills = {"Python", "SQL", "Git"}
skills.add("Pandas")
skills.discard("Missing")  # Safe remove

other = {"SQL", "JavaScript"}

print("\n=== Sets ===")
print(skills | other)  # Union
print(skills & other)  # Intersection
print(skills - other)  # Difference

# -------------------------------------------------------
# Comprehensions
# -------------------------------------------------------
squares = {x: x**2 for x in range(6)}
unique_letters = {c for c in "mississippi" if c in "sip"}

print("\nComprehensions:")
print(squares)
print(unique_letters)

# -------------------------------------------------------
# Motivation
# -------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "="*60)
    print("LESSON 3 COMPLETE - DECEMBER 31, 2025")
    print("="*60)
    print("Dictionaries organize your goals. Sets remove doubt.")
    print("2026 is here. Your streak continues. 🚀")

# SELF-TEST QUIZ (10 questions) - answers in comments below
"""
1. How to safely get a dict value?
2. What does set1 | set2 do?
3. True/False: Dicts preserve insertion order (Python 3.7+)
4. Fix: profile["missing"] = value (safe way)
5. Create set from duplicates: {1,1,2,2,3}
6. Dict comprehension for word lengths
7. What does .pop() return?
8. "Python" in skills vs "Python" in profile
9. How to check if key exists in dict
10. Create dict from two lists

# Answers:
# 1. .get(key, default)
# 2. Union
# 3. True
# 4. profile.setdefault("missing", value)
# 5. {1,2,3}
# 6. {w: len(w) for w in words}
# 7. Value (or default)
# 8. Set membership vs dict key
# 9. key in dict
# 10. dict(zip(keys, values))
"""