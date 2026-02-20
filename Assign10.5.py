#Task 1 – Variable Naming Issues .Improve unclear variable and function names using AI. The given function uses unclear variable names (f, a, b), which reduce readability and maintainability.
def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


print(add_numbers(10, 20))


#Task 2: Missing Error Handling. Add proper exception handling. The original code crashes when dividing by zero because no error handling is implemented.
def divide_numbers(numerator, denominator):
    """Divide two numbers with error handling."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type."


print(divide_numbers(10, 0))

#Task 3:  Student Marks Processing System. Refactor code to follow PEP 8 standards and improve readability. The original program lacks structure, meaningful variable names, and input validation.
def calculate_grade(marks):
    """
    Calculate total, average, and grade based on marks list.
    """
    if not marks:
        return "No marks provided."

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    else:
        grade = "F"

    return total_marks, average_marks, grade


marks_list = [78, 85, 90, 66, 88]
result = calculate_grade(marks_list)

if isinstance(result, tuple):
    total, average, grade = result
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
else:
    print(result)
    

#Task 4: Adding Docstrings and Inline Comments. Add documentation and comments. The factorial function lacks documentation and explanatory comments.
def factorial(number):
    """
    Calculate the factorial of a non-negative integer.
    
    Parameters:
    number (int): A non-negative integer
    
    Returns:
    int: Factorial of the number
    """
    if number < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, number + 1):
        result *= i  # Multiply result by current number

    return result


print(factorial(5))


#Task 5: Enhanced Password Validation System. Improve password validation with stronger security rules. The original code checks only minimum length, which is insufficient for security
import re
def validate_password(password):
    """
    Validate password strength based on multiple security rules.
    Returns True if strong, otherwise False.
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


user_password = input("Enter password: ")

if validate_password(user_password):
    print("Strong Password")
else:
    print("Weak Password")