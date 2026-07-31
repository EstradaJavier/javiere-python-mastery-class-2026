from datetime import date, datetime


def show_intro():
    """
    Print the lesson title and learning goals.
    """
    print("Welcome to Python Mastery 2026 - Lesson 1: Basics")
    print("In this lesson, you will practice core Python foundations.")
    print("We will explore variables, data types, strings, math,")
    print("functions, conditionals, and beginner-friendly self-tests.\n")


def calculate_age_from_dob(dob: date) -> int:
    """
    Calculate age from date of birth.
    """
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def get_dob_from_user() -> date:
    """
    Ask the user to enter a date of birth in YYYY-MM-DD format.
    """
    dob_input = input("Enter your DOB (YYYY-MM-DD): ")
    return datetime.strptime(dob_input, "%Y-%m-%d").date()


def create_profile(use_input=False):
    """
    Create a beginner-friendly personal profile.
    """
    name = "Javier"
    eye_color = "green"
    blood_type = "O-"
    is_married = True
    spouse_name = "Alesha"
    height_feet = 5
    height_inches = 10
    total_inches = (height_feet * 12) + height_inches
    height_meters = round(total_inches * 0.0254, 2)
    dob = get_dob_from_user() if use_input else date(1963, 2, 9)
    age = calculate_age_from_dob(dob)

    return (
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
    )


def display_profile(
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
):
    """
    Print the user's profile and show the type of each value.
    """
    print("===== PROFILE INFORMATION =====")
    print(f"Name: {name} (type: {type(name)})")
    print(f"Date of birth: {dob} (type: {type(dob)})")
    print(f"Age: {age} (type: {type(age)})")
    print("Age: {} (type: {})".format(age, type(age)))
    print(f"Height: {height_feet}'{height_inches}\" / {height_meters} m")
    print(f"Eye color: {eye_color} (type: {type(eye_color)})")
    print(f"Blood type: {blood_type} (type: {type(blood_type)})")
    print(f"Married: {is_married} (type: {type(is_married)})")
    print(f"Spouse: {spouse_name} (type: {type(spouse_name)})\n")


def explain_basic_data_types(age, height_meters, eye_color, is_married):
    """
    Show common beginner data types.
    """
    print("===== BASIC DATA TYPES =====")
    print(f"Integer example: age = {age}")
    print("Integers are whole numbers like 1, 25, and 100.\n")
    print(f"Float example: height_meters = {height_meters}")
    print("Floats are numbers with decimals like 1.5 or 3.14.\n")
    print(f"String example: eye_color = '{eye_color}'")
    print("Strings are text values inside quotes.\n")
    print(f"Boolean example: is_married = {is_married}")
    print("Booleans are only True or False.\n")


def string_examples(name, eye_color, spouse_name):
    """
    Demonstrate beginner string operations.
    """
    print("===== STRING EXAMPLES =====")
    print("Concatenation:")
    print(name + " has " + eye_color + " eyes.\n")
    print("f-string:")
    print(f"{name} is married to {spouse_name}.\n")
    print("String methods:")
    print(f"Uppercase name: {name.upper()}")
    print(f"Lowercase eye color: {eye_color.lower()}")
    print(f"Spouse name length: {len(spouse_name)} characters\n")


def run_operations(age, height_meters):
    """
    Demonstrate basic arithmetic operations.
    """
    print("===== BASIC OPERATIONS =====")
    years_to_retirement = 65 - age
    height_feet_decimal = round(height_meters * 3.28084, 2)
    print(f"Years to retirement at age 65: {years_to_retirement}")
    print(f"Height in decimal feet: {height_feet_decimal}")
    print(f"Age plus 10 years: {age + 10}")
    print(f"Age minus 5 years: {age - 5}")
    print(f"Age multiplied by 2: {age * 2}")
    print(f"Age divided by 2: {age / 2}\n")
    return years_to_retirement, height_feet_decimal


def type_conversion_examples(age, blood_type):
    """
    Show how Python can convert values from one type to another.
    """
    print("===== TYPE CONVERSION =====")
    age_as_string = str(age)
    sample_number_text = "42"
    converted_number = int(sample_number_text)
    print(f"Age as string: {age_as_string} (type: {type(age_as_string)})")
    print(
        f"Text '42' converted to int: {converted_number} "
        f"(type: {type(converted_number)})"
    )
    print(f"Blood type stays a string: {blood_type} (type: {type(blood_type)})\n")


def conditional_examples(age, is_married):
    """
    Demonstrate if / elif / else logic.
    """
    print("===== CONDITIONAL EXAMPLES =====")
    if age < 18:
        print("Minor: under 18")
    elif age < 65:
        print("Adult: between 18 and 64")
    else:
        print("Senior: 65 or older")

    if is_married:
        print("Marital status: Married")
    else:
        print("Marital status: Not married")

    print()


def list_examples():
    """
    Introduce a list and a simple loop.
    """
    print("===== LIST EXAMPLES =====")
    favorite_topics = [
        "Python basics",
        "Variables",
        "Strings",
        "Functions",
        "Conditionals",
    ]
    print(f"List: {favorite_topics}")
    print(f"First item: {favorite_topics[0]}")
    print(f"Number of items: {len(favorite_topics)}")
    print("Looping through the list:")
    for topic in favorite_topics:
        print(f"- {topic}")
    print()


def visual_map():
    """
    Show the learner the program flow.
    """
    print("===== VISUAL MAP OF THIS PROGRAM =====")
    print("main()")
    print("  -> show_intro()")
    print("  -> create_profile()")
    print("  -> display_profile()")
    print("  -> explain_basic_data_types()")
    print("  -> string_examples()")
    print("  -> run_operations()")
    print("  -> type_conversion_examples()")
    print("  -> conditional_examples()")
    print("  -> list_examples()")
    print("  -> beginner_practice_snippets()")
    print("  -> assert_fail_examples()")
    print("  -> self_test()")
    print()


def assert_fail_examples():
    """
    Show examples of assertions that fail on purpose.
    """
    print("===== ASSERT FAIL EXAMPLES =====")
    try:
        test_age = -5
        assert test_age >= 0, "Assertion failed: age should never be negative."
    except AssertionError as error:
        print(error)
        print("Why it failed: -5 is less than 0, so the condition is False.\n")

    try:
        test_height = 0.0
        assert test_height > 0, "Assertion failed: height must be greater than zero."
    except AssertionError as error:
        print(error)
        print("Why it failed: 0.0 is not greater than 0, so the condition is False.\n")

    try:
        test_name = ""
        assert len(test_name) > 0, "Assertion failed: name should not be empty."
    except AssertionError as error:
        print(error)
        print("Why it failed: an empty string has length 0, so the condition is False.\n")

    try:
        test_age_for_retirement = 63
        test_years_to_retirement = 10
        assert test_years_to_retirement == 65 - test_age_for_retirement, (
            "Assertion failed: retirement calculation is incorrect."
        )
    except AssertionError as error:
        print(error)
        print("Why it failed: 65 - 63 equals 2, not 10, so the condition is False.\n")


def self_test(name, age, height_meters, years_to_retirement):
    """
    Run simple checks to make sure the important values make sense.
    """
    print("===== SELF-TEST =====")
    assert isinstance(name, str), "Name should be a string."
    assert isinstance(age, int), "Age should be an integer."
    assert isinstance(height_meters, float), "Height in meters should be a float."
    assert age > 0, "Age must be positive."
    assert years_to_retirement == 65 - age, "Retirement calculation failed."
    assert len(name) > 0, "Name should not be empty."
    print("All self-tests passed. Great job — the basics are working.\n")


def beginner_practice_snippets():
    """
    Show a few small examples for beginners to study.
    """
    print("===== EXTRA PRACTICE SNIPPETS =====")
    print("Snippet 1: Variable reassignment")
    score = 10
    print(f"Starting score: {score}")
    score = score + 5
    print(f"Updated score: {score}\n")

    print("Snippet 2: Comparing values")
    a = 7
    b = 10
    print(f"Is a greater than b? {a > b}")
    print(f"Is a less than b? {a < b}")
    print(f"Is a equal to b? {a == b}\n")

    print("Snippet 3: A very small function")

    def add_numbers(x, y):
        return x + y

    print(f"add_numbers(5, 4) = {add_numbers(5, 4)}\n")


def main():
    """
    Control the order of the lesson.
    """
    show_intro()
    visual_map()

    use_input = False

    (
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
    ) = create_profile(use_input)

    display_profile(
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
    )

    explain_basic_data_types(age, height_meters, eye_color, is_married)
    string_examples(name, eye_color, spouse_name)
    years_to_retirement, height_feet_decimal = run_operations(age, height_meters)
    type_conversion_examples(age, blood_type)
    conditional_examples(age, is_married)
    list_examples()
    beginner_practice_snippets()
    assert_fail_examples()
    self_test(name, age, height_meters, years_to_retirement)

    print("Lesson 1 complete.")
    print("Review the comments, rerun the program, and experiment with values.")
    print("Try changing a variable and predict what the output will be before running it.")


if __name__ == "__main__":
    main()