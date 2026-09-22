# Top 40 Most Used Python Functions

A practical reference of the most frequently used built-in functions and common methods in Python, with clear purposes
and short examples.

| Function                      | Purpose                                                | Example                                                 |
|-------------------------------|--------------------------------------------------------|---------------------------------------------------------|
| `print()`                     | Displays output to the console                         | `print("Hello, world!")`                                |
| `len()`                       | Returns the number of items in an object               | `len([1, 2, 3])  # 3`                                   |
| `range()`                     | Generates a sequence of numbers                        | `list(range(5))  # [0, 1, 2, 3, 4]`                     |
| `type()`                      | Returns the type of an object                          | `type(42)  # <class 'int'>`                             |
| `isinstance()`                | Checks if an object is an instance of a class          | `isinstance(3.14, float)  # True`                       |
| `open()`                      | Opens a file and returns a file object                 | `with open("file.txt") as f: ...`                       |
| `input()`                     | Reads a line of text from the user                     | `name = input("Enter name: ")`                          |
| `sum()`                       | Returns the sum of all items in an iterable            | `sum([1, 2, 3, 4])  # 10`                               |
| `max()`                       | Returns the largest item                               | `max(5, 12, 3)  # 12`                                   |
| `min()`                       | Returns the smallest item                              | `min(5, 12, 3)  # 3`                                    |
| `sorted()`                    | Returns a new sorted list from an iterable             | `sorted([3, 1, 2])  # [1, 2, 3]`                        |
| `enumerate()`                 | Adds a counter to an iterable                          | `list(enumerate(["a", "b"]))  # [(0, 'a'), (1, 'b')]`   |
| `zip()`                       | Combines multiple iterables element-wise               | `list(zip([1, 2], ["a", "b"]))  # [(1, 'a'), (2, 'b')]` |
| `map()`                       | Applies a function to every item of an iterable        | `list(map(str, [1, 2, 3]))  # ['1', '2', '3']`          |
| `filter()`                    | Filters items using a function that returns True/False | `list(filter(lambda x: x > 0, [-1, 2, 0]))  # [2]`      |
| `list()`                      | Creates a list (or converts an iterable to a list)     | `list("abc")  # ['a', 'b', 'c']`                        |
| `dict()`                      | Creates a dictionary                                   | `dict(a=1, b=2)  # {'a': 1, 'b': 2}`                    |
| `set()`                       | Creates a set of unique elements                       | `set([1, 2, 2, 3])  # {1, 2, 3}`                        |
| `str()`                       | Converts a value to a string                           | `str(123)  # '123'`                                     |
| `int()`                       | Converts a value to an integer                         | `int("42")  # 42`                                       |
| `float()`                     | Converts a value to a floating-point number            | `float("3.14")  # 3.14`                                 |
| `bool()`                      | Converts a value to a Boolean                          | `bool(0)  # False`                                      |
| `abs()`                       | Returns the absolute value of a number                 | `abs(-7)  # 7`                                          |
| `round()`                     | Rounds a number to a given precision                   | `round(3.14159, 2)  # 3.14`                             |
| `any()`                       | Returns True if any element is truthy                  | `any([0, False, 5])  # True`                            |
| `all()`                       | Returns True if all elements are truthy                | `all([1, True, "hi"])  # True`                          |
| `list.append()`               | Adds an item to the end of a list                      | `nums = [1, 2]; nums.append(3)  # [1, 2, 3]`            |
| `list.extend()`               | Adds all items from an iterable to a list              | `a = [1]; a.extend([2, 3])  # [1, 2, 3]`                |
| `list.insert()`               | Inserts an item at a specific position                 | `a = [1, 3]; a.insert(1, 2)  # [1, 2, 3]`               |
| `list.pop()`                  | Removes and returns an item at a given index           | `a = [1, 2, 3]; a.pop()  # returns 3`                   |
| `list.remove()`               | Removes the first occurrence of a value                | `a = [1, 2, 3]; a.remove(2)  # [1, 3]`                  |
| `dict.get()`                  | Returns the value for a key, or a default              | `d = {"a": 1}; d.get("b", 0)  # 0`                      |
| `dict.keys()`                 | Returns a view of the dictionary’s keys                | `list({"a": 1, "b": 2}.keys())  # ['a', 'b']`           |
| `dict.values()`               | Returns a view of the dictionary’s values              | `list({"a": 1, "b": 2}.values())  # [1, 2]`             |
| `dict.items()`                | Returns a view of key-value pairs                      | `list({"a": 1}.items())  # [('a', 1)]`                  |
| `str.split()`                 | Splits a string into a list by a separator             | `"a,b,c".split(",")  # ['a', 'b', 'c']`                 |
| `str.join()`                  | Joins elements of an iterable into a string            | `",".join(["a", "b", "c"])  # 'a,b,c'`                  |
| `str.strip()`                 | Removes leading and trailing whitespace                | `"  hello  ".strip()  # 'hello'`                        |
| `str.replace()`               | Replaces occurrences of a substring                    | `"hello".replace("l", "L")  # 'heLLo'`                  |
| `str.upper()` / `str.lower()` | Converts a string to upper or lower case               | `"Hi".upper()  # 'HI'`                                  |

---

**Notes**

- Methods are shown with their type prefix (e.g. `list.append()`) for clarity.
- Examples are short and focused on the most common usage.
- This list prioritizes everyday built-ins and the most frequently used methods on lists, dictionaries, and strings.
