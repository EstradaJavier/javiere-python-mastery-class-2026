"""
Module 02 - Intermediate Python
Lesson 01 - Callback Functions

This lesson introduces callback functions in a beginner-friendly way.

A callback function is simply:
- a function that we pass into another function
- so that the other function can call it later

This is an important intermediate Python idea because it teaches that
functions are "first-class objects" in Python. That means a function
can be stored in a variable, passed as an argument, and returned from
another function.

This file is intentionally written with many comments so a beginner can
read it slowly and understand both the "what" and the "why."
"""


# ============================================================
# SECTION 1: A VERY SIMPLE CALLBACK EXAMPLE
# ============================================================
#
# In this first section, we start with the smallest useful example.
# The goal is to show the basic pattern before adding more detail.
#
# Pattern:
# 1. Write a regular function.
# 2. Pass that function into another function.
# 3. Let the second function call the first one later.
#


def say_hello(name):
    """
    Return a simple greeting string.

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def run_callback(callback_function, value):
    """
    Accept another function as an argument and call it.

    Parameters:
        callback_function: A function that will be called later.
        value: The value that will be passed into the callback function.

    Returns:
        Whatever the callback function returns.
    """
    return callback_function(value)


# ============================================================
# SECTION 2: MORE THAN ONE CALLBACK
# ============================================================
#
# The power of callbacks comes from flexibility.
# We can keep the "main" function the same, but change the behavior
# by passing in a different callback.
#


def make_uppercase(text):
    """
    Convert text to uppercase.
    """
    return text.upper()


def add_excitement(text):
    """
    Add excitement marks to text.
    """
    return f"{text}!!!"


def transform_text(text, callback_function):
    """
    Apply a callback to the given text.

    This function does not need to know HOW the text will change.
    It only knows that it has been given a function to call.
    """
    return callback_function(text)


# ============================================================
# SECTION 3: REAL-WORLD STYLE EXAMPLE
# ============================================================
#
# Here we simulate a simple "task completed" pattern.
# In real software, one part of a program often finishes some work
# and then calls another function to react to that event.
#


def on_task_complete(task_name):
    """
    Build a message that says a task is complete.
    """
    return f"Task completed: {task_name}"


def complete_task(task_name, completion_callback):
    """
    Pretend to complete a task, then call the callback function.
    """
    return completion_callback(task_name)


# ============================================================
# SECTION 4: LESSON DEMONSTRATION
# ============================================================
#
# This function groups the demonstrations together so that main()
# stays neat and easy to read.
#


def lesson_demo():
    """
    Run all callback lesson demonstrations and return the results.

    Returning data instead of only printing it makes the code easier
    to test with pytest later.
    """
    greeting_result = run_callback(say_hello, "Javier")

    uppercase_result = transform_text("python callbacks", make_uppercase)

    excited_result = transform_text("learning is working", add_excitement)

    task_result = complete_task("Read the callback lesson", on_task_complete)

    return {
        "greeting_result": greeting_result,
        "uppercase_result": uppercase_result,
        "excited_result": excited_result,
        "task_result": task_result,
    }


# ============================================================
# SECTION 5: MAIN FUNCTION
# ============================================================
#
# This prints the results in a beginner-friendly way so the learner
# can run the file and immediately see what happened.
#


def main():
    """
    Run the callback lesson demonstration.
    """
    print("=" * 60)
    print("MODULE 02 - LESSON 01: CALLBACK FUNCTIONS")
    print("=" * 60)
    print()

    print("A callback function is a function passed into another")
    print("function so it can be called later.")
    print()

    results = lesson_demo()

    print("Example 1 - Basic callback:")
    print(results["greeting_result"])
    print()

    print("Example 2 - Same function, different callback behavior:")
    print(results["uppercase_result"])
    print(results["excited_result"])
    print()

    print("Example 3 - Event-style callback:")
    print(results["task_result"])
    print()

    print("Lesson complete.")
    print("You have now seen how one function can receive another")
    print("function and call it later.")
    print()


if __name__ == "__main__":
    main()
