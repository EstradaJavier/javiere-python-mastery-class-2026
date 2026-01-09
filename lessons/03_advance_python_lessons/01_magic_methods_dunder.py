# 01_magic_methods_dunder.py
# Lesson 01 in 03_advanced_python_lessons: Magic Methods (Dunder Methods)
# Goal: Learn how to customize object behavior using special methods (double underscore).
# These are called "dunder" methods: __init__, __str__, __len__, __add__, etc.
# They let your custom classes work like built-in types (lists, strings, numbers).

class Vector:
    """A simple 2D vector class that supports common operations via magic methods."""

    def __init__(self, x, y):
        """Constructor - called when you create an object."""
        self.x = x
        self.y = y

    def __str__(self):
        """String representation for print() and str()."""
        # Called when you do print(vector) or str(vector)
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Official representation - used in REPL/debuggers."""
        # Goal: Make it possible to recreate the object from the string
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        """Called by len() - returns the 'length' of the object."""
        # Here: number of components (always 2 for 2D vector)
        return 2

    def __add__(self, other):
        """Called when you do vector1 + vector2."""
        # Supports adding two vectors (component-wise)
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add Vector to another Vector")

    def __eq__(self, other):
        """Called when you do vector1 == vector2."""
        # Equality check: same x and y
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __abs__(self):
        """Called by abs() - returns the magnitude (length) of the vector."""
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __getitem__(self, index):
        """Allows indexing: vector[0] returns x, vector[1] returns y."""
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError("Index out of range")


# === Examples & Expected Results ===

v1 = Vector(3, 4)
v2 = Vector(1, 2)

# __str__ and __repr__
print(v1)                       # Expected: Vector(3, 4)
print(repr(v1))                 # Expected: Vector(3, 4)
# In REPL/debugger, you'd see Vector(3, 4) too

# __len__
print(len(v1))                  # Expected: 2

# __add__
v3 = v1 + v2
print(v3)                       # Expected: Vector(4, 6)

# __eq__
print(v1 == Vector(3, 4))       # Expected: True
print(v1 == v2)                 # Expected: False

# __abs__ (magnitude)
print(abs(v1))                  # Expected: 5.0 (since sqrt(3² + 4²) = 5)

# __getitem__ (indexing)
print(v1[0])                    # Expected: 3
print(v1[1])                    # Expected: 4
# print(v1[2])                  # Would raise IndexError

# Summary of all expected outputs when run:
# Vector(3, 4)
# Vector(3, 4)
# 2
# Vector(4, 6)
# True
# False
# 5.0
# 3
# 4