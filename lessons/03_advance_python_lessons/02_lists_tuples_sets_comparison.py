# 02_lists_tuples_sets_comparison.py
# Lesson 02 in 03_advanced_python_lessons: Lists vs Tuples vs Sets - Visually Explained
# Goal: Deep comparison of Python's three main sequence/collection types.
# We'll cover creation, mutability, ordering, duplicates, performance, and when to use each.
# Heavy comments + visual analogies + examples + expected outputs.

# === Quick Visual Summary (Mental Model) ===
# List:    [ordered, mutable, allows duplicates]      → Like a shopping list you can edit anytime
# Tuple:   (ordered, immutable, allows duplicates)    → Like a fixed ticket: can't change after printing
# Set:     {unordered, mutable, NO duplicates}        → Like a unique guest list: no repeats, order doesn't matter

# === 1. Creation Syntax ===
list_example = [1, 2, 3, 2, 'apple']          # Square brackets []
tuple_example = (1, 2, 3, 2, 'apple')         # Parentheses ()
set_example   = {1, 2, 3, 2, 'apple'}         # Curly braces {} — duplicates auto-removed!

print("List:  ", list_example)   # Expected: [1, 2, 3, 2, 'apple']
print("Tuple: ", tuple_example)  # Expected: (1, 2, 3, 2, 'apple')
print("Set:   ", set_example)    # Expected: {1, 2, 3, 'apple'}  ← duplicate 2 removed!

# === 2. Mutability (Can we change after creation?) ===
# List: Yes – mutable
list_example.append(99)           # Add item
list_example[0] = 100             # Change item
print("Modified List:", list_example)  # Expected: [100, 2, 3, 2, 'apple', 99]

# Tuple: No – immutable (can't change)
# tuple_example[0] = 100          # TypeError: 'tuple' object does not support item assignment
# tuple_example.append(99)        # AttributeError: 'tuple' object has no attribute 'append'

# Set: Yes – mutable, but elements must be immutable
set_example.add(99)               # Add
set_example.remove(1)             # Remove
print("Modified Set:", set_example)  # Expected: {2, 3, 'apple', 99} (order random)

# === 3. Ordering & Indexing ===
# List & Tuple: Ordered – you can access by index
print(list_example[0])           # 100
print(tuple_example[2])          # 3

# Set: Unordered – NO index access
# print(set_example[0])          # TypeError: 'set' object is not subscriptable

# === 4. Duplicates ===
print("List allows duplicates:", [1,1,1])      # [1, 1, 1]
print("Tuple allows duplicates:", (1,1,1))     # (1, 1, 1)
print("Set removes duplicates:", {1,1,1})      # {1}

# === 5. Performance & Use Cases ===
# List: Good for ordered, changeable collections (most common)
# Tuple: Faster & safer when data shouldn't change (function returns, dictionary keys)
# Set: Fastest for membership checks & removing duplicates (O(1) lookup)

# Example: Remove duplicates from a list quickly
duplicates = [5, 3, 8, 5, 3, 1]
unique = list(set(duplicates))  # Convert to set → removes dups → back to list
print("Unique values:", unique)  # Expected: [5, 3, 8, 1] (order may vary)

# Tuple as dictionary key (lists/sets can't be keys)
coords = {(10, 20): "Point A"}  # Valid – tuple is immutable
# [10, 20]: "Point B"           # TypeError: unhashable type: 'list'

# === 6. Memory & Speed Comparison (Quick Test) ===
import sys
print("Memory - List: ", sys.getsizeof([1,2,3,4,5]))    # Usually ~88-120 bytes
print("Memory - Tuple:", sys.getsizeof((1,2,3,4,5)))    # Usually ~80-96 bytes (smaller!)
print("Memory - Set:  ", sys.getsizeof({1,2,3,4,5}))    # Usually ~216 bytes (larger due to hash table)

# Summary Table (visual reference)
print("""
Key Differences:
Feature       | List          | Tuple         | Set
--------------|---------------|---------------|--------------------
Mutable       | Yes           | No            | Yes
Ordered       | Yes           | Yes           | No
Duplicates    | Yes           | Yes           | No
Indexing      | Yes           | Yes           | No
Use Case      | Dynamic lists | Fixed data    | Unique items, fast lookup
""")

# Expected overall output highlights:
# List:   [1, 2, 3, 2, 'apple']
# Tuple:  (1, 2, 3, 2, 'apple')
# Set:    {1, 2, 3, 'apple'}
# Modified List: [100, 2, 3, 2, 'apple', 99]
# Unique values: [5, 3, 8, 1] (or similar order)