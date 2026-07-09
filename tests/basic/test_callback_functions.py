"""
Tests for Module 02 - Lesson 01 - Callback Functions

These tests are intentionally simple and beginner-friendly.
They focus on return values, because return values are easier
to test than printed output.
"""

from pathlib import Path
import importlib.util

lesson_path = Path("lessons/02_intermediate_python_lessons/01_callback_functions.py")

spec = importlib.util.spec_from_file_location("callback_lesson", lesson_path)
callback_lesson = importlib.util.module_from_spec(spec)
spec.loader.exec_module(callback_lesson)

add_excitement = callback_lesson.add_excitement
complete_task = callback_lesson.complete_task
lesson_demo = callback_lesson.lesson_demo
make_uppercase = callback_lesson.make_uppercase
on_task_complete = callback_lesson.on_task_complete
run_callback = callback_lesson.run_callback
say_hello = callback_lesson.say_hello
transform_text = callback_lesson.transform_text


def test_say_hello_returns_greeting():
    """
    Test that say_hello returns the expected greeting.
    """
    assert say_hello("Javier") == "Hello, Javier!"


def test_run_callback_calls_passed_function():
    """
    Test that run_callback correctly calls the function it receives.
    """
    assert run_callback(say_hello, "Ana") == "Hello, Ana!"


def test_make_uppercase_changes_text():
    """
    Test that make_uppercase converts text to uppercase.
    """
    assert make_uppercase("python") == "PYTHON"


def test_add_excitement_adds_exclamation_marks():
    """
    Test that add_excitement adds three exclamation marks.
    """
    assert add_excitement("Great job") == "Great job!!!"


def test_transform_text_with_uppercase_callback():
    """
    Test transform_text with the make_uppercase callback.
    """
    assert transform_text("callbacks", make_uppercase) == "CALLBACKS"


def test_transform_text_with_excitement_callback():
    """
    Test transform_text with the add_excitement callback.
    """
    assert transform_text("learning", add_excitement) == "learning!!!"


def test_complete_task_uses_callback():
    """
    Test that complete_task uses the completion callback correctly.
    """
    assert complete_task("Practice Python", on_task_complete) == "Task completed: Practice Python"


def test_lesson_demo_returns_expected_dictionary_values():
    """
    Test the grouped lesson demonstration results.
    """
    results = lesson_demo()

    assert results["greeting_result"] == "Hello, Javier!"
    assert results["uppercase_result"] == "PYTHON CALLBACKS"
    assert results["excited_result"] == "learning is working!!!"
    assert results["task_result"] == "Task completed: Read the callback lesson"
